class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    if n < 1:
      return False
    
    if n.bit_count() != 1:
      return False
    n = bin(n)[2:]

    count = 0
    for ch in n:
      if ch == '0':
        count += 1

    if count % 2 != 0:
      return False
    
    return True