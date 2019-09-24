#Class For Linked List Node
class Node:
    #This is Class Constructor
    def __init__(self,data):
        # Node Data
        self.data = data
        # Next Data Pointer default as None
        self.next = None
# Class For Linked List Operations
class LinkedList:
     #This is Class Constructor
    def __init__(self):
        # Linked List Head default as None
        self.head = None

    # Insert Node on Head
    def insertHead(self,data):
        # Checking Linked List is Empty 
        if self.head is None:
            self.head = Node(data) # <= Creating Node Class Object with passing Data
        else:
            temp = self.head # <= Store old data on temp variable
            self.head = Node(data) #<= Set New data as Head Node
            self.head.next = temp # <= Set Head node's next node

    def insertEnd(self,data):
        if self.head is None:
            self.insertHead(data) # <= if list is empty than create head node
        else:
            self.head.next = Node(data) #<= Set last node's next node as new data


    # View Linked List 
    def viewList(self):
        if self.head is None:                   # <= Checking is Head is Empty That mean Linked List is Empty
            print("Linked List is Empty")
        else:
            currentNode = self.head     # Set Head node on currentNode Variable
            while currentNode is not None:   # While loop.... when current node is None than stop
                print(currentNode.data,end=" => ")  # => Printing Current Node Data
                currentNode = currentNode.next      # Increment Current Node



if __name__ == '__main__':      

    l = LinkedList()        # Creatinf Linked List Class Object


    l.insertEnd("Mahamad")  # Inserting New Data on Linklist at end
    l.insertEnd("Shamem")   # Inserting New Data on Linklist at end

    l.insertHead("Nasim")   # Inserting New Data on Linklist at Head

    l.viewList()            # Printing Linked list all Data (Nasim => Mahamad => Shamem =>)
    
