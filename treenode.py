# Codecademy - CS102: Data Structures and Algorithms - Final Project
# Tree node class

class TreeNode:    
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.height = 0

    def hasLeftChild(self):
        if self.leftChild:
            return True
        return False

    def hasRightChild(self):
        if self.rightChild:
            return True
        return False

    def isLeftChild(self):
        if self.parent and self.parent.leftChild == self:
            return True
        return False

    def isRightChild(self):
        if self.parent and self.parent.rightChild == self:
            return True
        return False

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        if self.leftChild or self.rightChild:
            return True
        return False

    def hasBothChildren(self):
        if self.leftChild and self.rightChild:
            return True
        return False