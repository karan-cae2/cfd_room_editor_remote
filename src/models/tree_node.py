class TreeNode:
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def child(self, row):
        return self.children[row]

    def childCount(self):
        return len(self.children)

    # --- ADD THIS METHOD ---
    def setValue(self, value):
        """Updates the node's stored value."""
        self.value = value