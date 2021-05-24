class Stack:

    def __init__ (self):
        self.date = []

    def insert (self, value):
        self.date.append (value)

    def pop (self):
       return self.date.pop ()

    def view (self):
        return self.date [len(self.date)-1]