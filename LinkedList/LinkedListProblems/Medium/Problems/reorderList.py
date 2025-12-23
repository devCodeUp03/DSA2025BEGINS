# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next        
#         prev = None
#         current = slow.next
#         slow.next = None
#         while current:
#             nxt = current.next
#             current.next = prev
#             prev = current
#             current = nxt        
#         current = prev
#         dummy = ListNode(0)
#         tail = dummy
#         list1 = head
#         list2 = current
#         while list1 and list2:
#             tail.next = list1
#             list1 = list1.next
#             tail = tail.next
#             tail.next = list2
#             list2 = list2.next
#             tail = tail.next        
#         tail.next = list1
#         head = dummy.next
            
        

        

        