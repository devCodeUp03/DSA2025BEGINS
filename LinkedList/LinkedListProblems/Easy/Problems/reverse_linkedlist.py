from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current = self.head
        
        while current != None:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        
        self.head = prev_node