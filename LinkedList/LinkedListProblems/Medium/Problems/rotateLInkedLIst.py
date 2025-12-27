# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if head is None:
#             return None
#         if head.next is None:
#             return head

#         initial = head
#         length = 0
#         while initial:
#             length+=1
#             initial = initial.next
#         k = k % length

#         dummy = ListNode(0)
#         dummy.next = head
        
#         for _ in range(k):
#             current = dummy.next
#             first = dummy.next

#             while current.next.next:
#                 current = current.next
            
#             dummy.next = current.next
#             current.next = None
#             dummy.next.next = first
        
#         return dummy.next

            