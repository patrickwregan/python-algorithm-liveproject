class BinaryNode:
    
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        
    def add_left(self, value):
        self.left_child = BinaryNode(value)
    
    def add_right(self, value ):
        self.right_child = BinaryNode(value)
    
    def __str__(self):
        if self.left_child == None and self.right_child == None:
            return f"{self.value}: None None"
        elif self.left_child == None:
            return f"{self.value}: None {self.right_child.value}"
        elif self.right_child == None:
            return f"{self.value}: {self.left_child.value} None"
        else:
            return f"{self.value}: {self.left_child.value} {self.right_child.value}"
        # return str(self.value) + " " + str(self.left_child.value) + " " + str(self.right_child.value) + "\n"

root = BinaryNode("Root")
root.add_left("A")
root.add_right("B")
A = root.left_child
A.add_left("C")
A.add_right("D")
C = A.left_child
D = A.right_child
B = root.right_child
B.add_right("E")
E = B.right_child
E.add_left("F")
F = E.left_child
print(root)
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)

