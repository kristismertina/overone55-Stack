class Stack:

    def __init__ (self):
        self.date = []

    def insert (self, value):
        self.date.append (value)

    def pop (self):
       return self.date.pop ()

    def view (self):
        return self.date [len(self.date)-1]

s = Stack()

print(s.list())
s.insert(4)
s.insert(2)
s.insert(8)
s.insert(3)
print(s.view())
print(s.pop())
print(s.view())
s.insert(6)
print(s.view())
print(s.pop())
print(s.view())