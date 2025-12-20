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
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data


ll = Linkedlist()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.insert_at_beginning(50)
ll.insert_at_beginning(60)



# ll.traverse_list()
middlenode = ll.middleNode()
print(middlenode)

