class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    max = 1162261467
    if n > 0 and max % n == 0:
      return True
    return False 