class Solution:
  def checkPerfectNumber(self, num: int) -> bool:
    if num <= 1:
      return False

    ans = 1
    for i in range(2, isqrt(num) + 1):
      if num % i == 0:
        ans += i
        pair = num // i
        if pair != i:
          ans += pair

    return ans == num