from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from models.tree_node import TreeNode


class TreeModel(QAbstractItemModel):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Root node
        self.root_node = TreeNode(
            key="root",
            value="Root",
            parent=None
        )

        # Room
        self.room_node = TreeNode(
            key="room1",
            value="Room",
            parent=self.root_node
        )

        # Room properties
        self.name_node = TreeNode(
            key="Name",
            value="Room A",
            parent=self.room_node
        )

        self.width_node = TreeNode(
            key="Width",
            value=10,
            parent=self.room_node
        )

        self.height_node = TreeNode(
            key="Height",
            value=5,
            parent=self.room_node
        )

        self.temperature_node = TreeNode(
            key="Temperature",
            value=25,
            parent=self.room_node
        )

        # Build the tree
        self.root_node.addChild(self.room_node)

        self.room_node.addChild(self.name_node)
        self.room_node.addChild(self.width_node)
        self.room_node.addChild(self.height_node)
        self.room_node.addChild(self.temperature_node)

    # --------------------------------------------------
    # How many columns?
    # --------------------------------------------------
    def columnCount(self, parent=QModelIndex()):
        return 2

    # --------------------------------------------------
    # How many rows?
    # --------------------------------------------------
    def rowCount(self, parent=QModelIndex()):

        if not parent.isValid():
            # Top level → root's children
            return self.root_node.childCount()

        # Get the TreeNode represented by this QModelIndex
        node = parent.internalPointer()

        return node.childCount()

    # --------------------------------------------------
    # Create QModelIndex for a row/column
    # --------------------------------------------------
    def index(self, row, column, parent=QModelIndex()):

        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parent_node = self.root_node
        else:
            parent_node = parent.internalPointer()

        child_node = parent_node.child(row)

        return self.createIndex(row, column, child_node)

    # --------------------------------------------------
    # What should be displayed?
    # --------------------------------------------------
    def data(self, index, role=Qt.DisplayRole):

        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        node = index.internalPointer()

        if index.column() == 0:
            return node.key

        if index.column() == 1:
            return str(node.value)

        return None

    # --------------------------------------------------
    # Parent of an item
    # --------------------------------------------------
    def parent(self, index):

        if not index.isValid():
            return QModelIndex()

        node = index.internalPointer()
        parent_node = node.parent

        if parent_node is None or parent_node == self.root_node:
            return QModelIndex()

        row = parent_node.parent.children.index(parent_node)

        return self.createIndex(
            row,
            0,
            parent_node
        )