# Given 2 seperated sorted linked lists, merge them together
# and retain the sorting

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    cur = ListNode(0)
    ans = cur

    while(l1 and l2):
      if(l1.val > l2.val):
        cur.next = l2
        l2 = l2.next
      else:
        cur.next = l1
        l1 = l1.next

      cur = cur.next

    while(l1):
      cur.next = l1
      l1 = l1.next
      cur = cur.next

    while(l2):
      cur.next = l2
      l2 = l2.next
      cur = cur.next

    return ans.next