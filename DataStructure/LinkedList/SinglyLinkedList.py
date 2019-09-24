#Creating Node For Our Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        currentNode = self.head
        count = 0
        while currentNode.next is not None:
            count += 1
            currentNode = currentNode.next
        return count
    
    
    def insertHead(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            tempHead = self.head
            self.head = Node(data)
            self.head.next = tempHead

    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            currentNode = self.head
            while True:
                if currentNode.next is None:
                    currentNode.next = Node(data)
                    break
                currentNode = currentNode.next

    def insertAt(self,position,data):
         # Check If Enter Position Exist
        if position < 0 or position > self.length():
            # Print Error Message
            print("Invalid Position") 

        elif self.length() == position:
            self.insert(data)

        # If User want to add node on Position 0 that mean it is Head Node
        elif position == 0 :
            self.insertHead(data)
        else:
            currentNode = self.head
            currentPositin = 0
            while True:
                if currentPositin == position:
                    x = priviousNode.next = Node(data)
                    x.next = currentNode
                    break
                priviousNode = currentNode
                currentNode = currentNode.next
                currentPositin +=1

    def delete(self):
        if self.head is not None:
            currentNode = self.head
            while currentNode.next is not None:
                priviousNode = currentNode
                currentNode = currentNode.next
            priviousNode.next = None
        else:
            print("There Is Nothing To Delete!")

    def deleteAt(self,position):
        if self.length() == position:
            self.deleteEnd()
        else:
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    #head =>[0]=>[1]=>[2]=>[3] ||  head =>[0]=>[1]=>__[3]__[2]none[3]
                    priviousNode.next = currentNode.next
                    currentNode.next = None
                    break

                priviousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1
    def viewList(self):
        if self.head is None:
            print("Opps! Linked List Is Empty")
        else:
            currentNode = self.head
            while currentNode is not None:
                print(currentNode.data,end="\n")
                currentNode = currentNode.next

if __name__ == '__main__':
    ll = LinkedList()

    ll.insert("Nasim")
    ll.insert("Mahamad")
    ll.insert("Dinajpur Polytechnic Institute")
    ll.viewList()
    print("______________")
    ll.insertAt(1,"Shamem")
    ll.viewList()
    print("______________")
    ll.deleteAt(2)
    ll.viewList()
