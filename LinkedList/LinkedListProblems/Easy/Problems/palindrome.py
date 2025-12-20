# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         # Step 1: find middle
#         slow = head
#         fast = head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         # Step 2: reverse second half
#         prev = None
#         current = slow

#         while current:
#             nxt = current.next
#             current.next = prev
#             prev = current
#             current = nxt

#         # Step 3: compare halves
#         left = head
#         right = prev

#         while right:
#             if left.val != right.val:
#                 return False
#             left = left.next
#             right = right.next

#         return True