class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(None, head)
    pre = dummy
    cur = head

    while cur:
      if cur.val == val:
        pre.next = cur.next
        cur = cur.next
        continue

      pre = cur
      cur = cur.next

    return dummy.next