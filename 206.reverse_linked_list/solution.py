class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
      return None
    
    cur = head
    prev = None
    while cur != None:
      _next = cur.next
      cur.next = prev
      prev = cur
      cur = _next

    return prev