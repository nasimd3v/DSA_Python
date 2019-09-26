class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self,data):
        self.items.insert(0,data)

    def deQueue(self):
        self.items.pop()

    def viewQueue(self):
        print(self.items)
      
    def size(self):
        print(len(self.items))

q = Queue()
q.enQueue("Shamem")
q.enQueue("Mahamad")
q.enQueue("Nasim")


q.viewQueue()
q.deQueue()
q.viewQueue()
