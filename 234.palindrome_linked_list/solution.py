class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    if head is None or head.next is None:
      return True
    
    slow = fast = head
    while fast.next != None and fast.next.next != None:
      slow = slow.next
      fast = fast.next.next

    mid = slow.next
    slow.next = None

    prev = None
    curr = mid

    while curr:
      nxt = curr.next
      curr.next = prev
      prev = curr
      curr = nxt

    right = prev
    left = head
    while right:
      if left.val != right.val:
          return False

      left = left.next
      right = right.next

    return True