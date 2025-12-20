class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        current = self.head

        while current != None:
            print(current.data)
            current = current.next

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        current = self.head
        while current.next != None:
            current = current.next

        current.next = new_node
    
    def insert_at_nth(self, data, position):
        new_node = Node(data)
        current = self.head

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        count = 1
        current = self.head
        while current and count < position - 1:
            current = current.next
            count+=1
        
        if current is None:
            print("Position unavailable/position out of range")
            return
        
        new_node.next = current.next
        current.next = new_node  

    def delete_at_beginning(self):
        if self.head == None:
            print("List is empty!")
            return

        self.head = self.head.next


    def delete_at_end(self):

        if self.head == None:
            print("List is empty")
            return      
    

        current = self.head

        if current.next == None:
            self.head = None
            return

        while current.next.next != None:
            current = current.next

        current.next = None

    def delete_at_nth(self, position):
        if self.head is None:
            print("List is empty!")
            return 
    
        
        if position == 1:
            self.head = self.head.next
            return
        
        current = self.head
        count = 1
        while current and count < position - 1:
            current = current.next
            count+=1
        
        if current is None:
            print(f"Position out of range")
            return
        
        current.next = current.next.next





        




ll = LinkedList()
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)


ll.delete_at_nth(1)

ll.traverse()

        
