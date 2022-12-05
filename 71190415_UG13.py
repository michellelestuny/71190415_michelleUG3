class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, self)
            else:
                self.right.insert(data)
        else:
            return False
        return True

class BinaryTree:
    def __init__(self):
        self.root = Node(0,None)
    def add(self, data):
        if self.root.left is None and data%2 != 0:
            self.root.left = Node(data,self.root)
        elif self.root.right is None and data%2 == 0:
            self.root.right = Node(data,self.root)
        else:
            if data%2 != 0:
                self.root.left.insert(data)
            else:
                self.root.right.insert(data)
    def sumGanjil(self,node,ganjil=[], sum = 0):   
        if node % 2 == 0:
            pass
        else:
            if node:
                sum = sum + ganjil
                a = sumGanjil(node.left, sum)
                b = sumGanjil(node.right, sum)

            if (node.left is None and node.right is None):
                ganjil.append(sum)

        return ganjil
   
    def hasilGanjil(self, root):
        if root:
            print(sumGanjil(root,sum))
if __name__ == '__main__':
    binaryT = BinaryTree()
    binaryT.add(5)
    binaryT.add(4)
    binaryT.add(3)
    binaryT.add(9)
    binaryT.add(8)
    binaryT.add(6)
    binaryT.add(7)
    binaryT.add(11)
    binaryT.add(10)
print()