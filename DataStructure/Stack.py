class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        self.stack.pop()
        
    def size(self):
        print(len(self.stack))
        
    def viewStack(self):
        print(self.stack)

stack = Stack()
stack.push("Nasim")
stack.push("Mahamad")
stack.push("Shamem")

stack.viewStack()
stack.pop()
stack.viewStack()
