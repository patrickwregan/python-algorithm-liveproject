
class NaryNode:
    
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        
    def __str__(self):
        str_result = f'{self.value}:'
        for item in self.children:
            str_result += f' {item.value}'
        return str_result
    



root = NaryNode("Root")
a = NaryNode("A")
b = NaryNode("B")
c = NaryNode("C")
d = NaryNode("D")
e = NaryNode("E")
f = NaryNode("F")
g = NaryNode("G")
h = NaryNode("H")
i = NaryNode("I")

root.add_child(a)
root.add_child(b)
root.add_child(c)
a.add_child(d)
a.add_child(e)
c.add_child(f)
d.add_child(g)
f.add_child(h)
f.add_child(i)

print(root)
print(a)
print(b)
print(c)
print(d)
print(f)
print(g)
print(h)
print(i)
