class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    curA = headA
    curB = headB

    while curA is not curB:
      if curA == None:
        curA = headB
      else:
        curA = curA.next
      if curB == None:
        curB = headA
      else:
        curB = curB.next
    
    return curA