# Given a linked list, remove the n-th node from the end of list
# and return its head.
#
# Input: 2
#     1 - 2 - 3 - 4 - 5
# Output:
#     1 - 2 - 3 - 5
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    ans = ListNode(0)
    ans.next = head

    first = ans
    second = ans

    # setting first pointer N+1
    for i in range(1, n+2);
      first = first.next

    #traversing the list until first reaches to null
    while (first is not None):
      first = first.next
      second = second.next

    second.next = second.next.next

    return ans.next