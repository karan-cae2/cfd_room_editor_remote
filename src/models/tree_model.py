from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from models.tree_node import TreeNode


class TreeModel(QAbstractItemModel):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.root_node = TreeNode(key="root", value="Root", parent=None)

        rooms_data = [
            {
                "key": "room1",
                "value": "Room A",
                "properties": {
                    "Width": 10,
                    "Height": 5,
                    "Temperature": 25
                }
            }
        ]

        # Build tree structure
        for room_info in rooms_data:
            room_node = TreeNode(
                key=room_info["key"],
                value=room_info["value"],
                parent=self.root_node
            )
            self.root_node.addChild(room_node)

            for prop_key, prop_val in room_info["properties"].items():
                prop_node = TreeNode(
                    key=prop_key,
                    value=prop_val,
                    parent=room_node
                )
                room_node.addChild(prop_node)

    # --------------------------------------------------
    # 1. Enable Editing Flags
    # --------------------------------------------------
    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        # Base flags for all items
        item_flags = Qt.ItemIsEnabled | Qt.ItemIsSelectable

        # Only allow Column 1 (Value column) to be edited
        if index.column() == 1:
            item_flags |= Qt.ItemIsEditable

        return item_flags

    # --------------------------------------------------
    # 2. Update Node Value when Edited
    # --------------------------------------------------
    def setData(self, index, value, role=Qt.EditRole):
        """Called automatically by Qt when the user finishes editing a cell."""
        if not index.isValid():
            return False

        # Ensure we are saving an actual edit edit role
        if role == Qt.EditRole:
            # 1. Get the target node
            node = index.internalPointer()

            # 2. Update the node's value property
            node.setValue(value)

            # 3. Notify Qt that the data at this index changed
            self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])
            return True

        return False

    # --------------------------------------------------
    # Basic Required QAbstractItemModel Methods
    # --------------------------------------------------
    def columnCount(self, parent=QModelIndex()):
        return 2

    def rowCount(self, parent=QModelIndex()):
        if not parent.isValid():
            return self.root_node.childCount()
        node = parent.internalPointer()
        return node.childCount()

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        parent_node = self.root_node if not parent.isValid() else parent.internalPointer()
        child_node = parent_node.child(row)
        return self.createIndex(row, column, child_node)

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        node = index.internalPointer()
        parent_node = node.parent
        if parent_node is None or parent_node == self.root_node:
            return QModelIndex()
        row = parent_node.parent.children.index(parent_node)
        return self.createIndex(row, 0, parent_node)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role in (Qt.DisplayRole, Qt.EditRole):
            node = index.internalPointer()
            if index.column() == 0:
                return node.key
            if index.column() == 1:
                return str(node.value)
        return None