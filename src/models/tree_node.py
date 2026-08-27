

class TreeNode:
    def __init__(self,key,value,parent):
        self.key=key
        self.value=value
        self.parent=parent
        self.children=[]

    def addChild(self,child):
        self.children.append(child)

    def child(self,row):
        child=self.children[row]
        return child

    def childCount(self):
        count=len(self.children)
        return count    