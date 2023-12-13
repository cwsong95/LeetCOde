# Reverse a singly linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node = None
    while(head is not None):
      next = head.next
      head.next = node
      node = head
      head = next
    return node