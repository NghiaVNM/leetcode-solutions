class Solution:
  def hasAlternatingBits(self, n: int) -> bool:
    n = bin(n)[2:]
    
    if len(n) == 1:
      return True
    
    prev = n[0]
    for i in range(1, len(n)):
      if n[i] == prev:
        return False
      else:
        prev = n[i]

    return True