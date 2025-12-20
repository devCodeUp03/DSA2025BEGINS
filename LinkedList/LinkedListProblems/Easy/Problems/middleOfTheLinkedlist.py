class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    
    def traverse_list(self):
        if self.head is None:
            print("list is empty")
            return
        
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
    def middleNode(self):
        current = self.head
        count = 0
        while current is not None:
            count+=1
            current = current.next
        
        middle = (count // 2) + 1
        print(middle)

        current = self.head
        i = 1
        while i < middle:
            current = current.next
            i+=1
        
        return current.data    



ll = Linkedlist()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.insert_at_beginning(50)
ll.insert_at_beginning(60)



ll.traverse_list()

middle = ll.middleNode()
print(middle)


        

        
        
