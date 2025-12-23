# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
#         st = set()
#         ha, hb = headA, headB

#         while ha:
#             st.add(ha)
#             ha = ha.next
        
#         while hb:
#             if hb in st:
#                 return hb
#             hb = hb.next
        
#         return hb
