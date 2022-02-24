# Codecademy - CS102: Data Structures and Algorithms - Final Project
# Binary search tree class

from treenode import TreeNode 
from string import capwords

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def getHeight(self, root):
        if not root:
            return -1
        return root.height

    def put(self, key, value):
        currentNode = self.root
        parent = None
        while currentNode != None:
            parent = currentNode
            if key < currentNode.key:
                currentNode = currentNode.leftChild
            else:
                currentNode = currentNode.rightChild
        if self.root == None:
            self.root = TreeNode(key, value)
        elif key < parent.key:
            parent.leftChild = TreeNode(key, value, parent=parent)
        else:
            parent.rightChild = TreeNode(key, value, parent=parent)
        self.size += 1

    def get(self, key):
        if self.root:
            self._get(key, self.root)
        else:
            return None
        
    def _get(self, key, currentNode): 
        if not currentNode:
            return None
        elif currentNode.key == key:
            if len(currentNode.payload) == 5:
                print(f"\n{capwords(str(currentNode.payload[0]))}\nSeason: {currentNode.payload[1]}\nLife cycle: {currentNode.payload[2]}\nColors: {currentNode.payload[3]}\nPet safe\n")
            else:
                print(f"\n{capwords(str(currentNode.payload[0]))}\nSeason: {currentNode.payload[1]}\nLife cycle: {currentNode.payload[2]}\nColors: {currentNode.payload[3]}\n")
            if currentNode.hasBothChildren():
                self._get(key, currentNode.leftChild), self._get(key, currentNode.rightChild)
            elif currentNode.hasLeftChild():
                self._get(key, currentNode.leftChild)
            elif currentNode.hasRightChild():
                self._get(key, currentNode.rightChild) 
        elif key < currentNode.key:
            self._get(key, currentNode.leftChild)
        else:
            self._get(key, currentNode.rightChild)

    def storeBSTNodes(self, root, nodes):
        if not root:
            return None
        self.storeBSTNodes(root.leftChild, nodes)
        nodes.append(root)
        self.storeBSTNodes(root.rightChild, nodes)

    def buildBST(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = nodes[mid]
        root.leftChild = self.buildBST(nodes, start, mid-1)
        root.rightChild = self.buildBST(nodes, mid+1, end)
        if root.hasBothChildren():
            root.height = 1 + max(self.getHeight(root.leftChild), self.getHeight(root.rightChild))
            balance = self.getBalance(root)
            if balance > 1 and root.key < root.leftChild.key:
                return self.rightRotate(root)
            if balance < -1 and root.key > root.rightChild.key:
                return self.leftRotate(root)
            if balance > 1 and root.key > root.leftChild.key:
                root.leftChild = self.leftRotate(root.leftChild)
                return self.rightRotate(root)
            if balance < -1 and root.key < root.rightChild.key:
                root.rightChild = self.rightRotate(root.rightChild)
                return self.leftRotate(root)
        elif root.hasLeftChild():
            root.height = 1 + self.getHeight(root.leftChild)
        elif root.hasRightChild():
            root.height = 1 + self.getHeight(root.rightChild)
        return root

    def balanceBST(self, root):
        nodes = []
        self.storeBSTNodes(root, nodes)
        n = len(nodes)
        root = self.buildBST(nodes, 0, n-1)
        root.parent = None
        self.parentNode(root)
        return root

    def parentNode(self, root):
        if root.hasBothChildren():
            root.leftChild.parent = root
            root.rightChild.parent = root
            self.parentNode(root.leftChild)
            self.parentNode(root.rightChild)
        elif root.hasLeftChild():
            root.leftChild.parent = root
            self.parentNode(root.leftChild)
        elif root.hasRightChild():
            root.rightChild.parent = root
            self.parentNode(root.rightChild)

    def getBalance(self, root):
        if not root:
            return None
        if root.hasBothChildren():
            return self.getHeight(root.leftChild) - self.getHeight(root.rightChild)
        elif root.hasLeftChild():
            return self.getHeight(root.leftChild)
        elif root.hasRightChild():
            return -(self.getHeight(root.rightChild))

    def leftRotate(self, root):
        right = root.rightChild
        tree = right.leftChild
        right.leftChild = root
        root.rightChild = tree
        lh = self.getHeight(root.leftChild)
        rh = self.getHeight(root.rightChild)
        rl = self.getHeight(right.leftChild)
        rr = self.getHeight(right.rightChild)
        root.height = 1 + max(lh, rh)
        right.height = 1 + max(rl, rr)
        return right

    def rightRotate(self, root):
        left = root.leftChild
        tree = left.rightChild
        left.rightChild = root
        root.leftChild = tree
        lh = self.getHeight(root.leftChild)
        rh = self.getHeight(root.rightChild)
        ll = self.getHeight(left.leftChild)
        lr = self.getHeight(left.rightChild)
        root.height = 1 + max(lh, rh)
        left.height = 1 + max(ll, lr)
        return left

    def preOrder(self, root):
        if root is not None:
            print("{0} {1} ".format(root.key, self.getHeight(root)),end="")
        if root.leftChild is not None:
            self.preOrder(root.leftChild)
        if root.rightChild is not None:
            self.preOrder(root.rightChild)
                        
    def inOrder(self, root):
        if root.leftChild is not None:
            self.inOrder(root.leftChild)
        if root is not None:
            print("{0} {1} ".format(root.key, self.getHeight(root)), end="")
        if root.rightChild is not None:
            self.inOrder(root.rightChild)

    def postOrder(self, root):
        if root.leftChild is not None:
            self.postOrder(root.leftChild)
        if root.rightChild is not None:
            self.postOrder(root.rightChild)
        if root is not None:
            print("{0} {1} ".format(root.key, self.getHeight(root)),end="")