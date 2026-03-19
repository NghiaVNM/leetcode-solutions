class Solution:
  def toHex(self, num: int) -> str:
    if num == 0:
      return '0'
    
    ans = ''

    if num < 0:
      num = num & 0xFFFFFFFF

    while num != 0:
      tmp = num % 16
      if tmp < 10:
        tmp += 48
      else:
        tmp += 55
      ans = chr(tmp) + ans
      num //= 16
    return ans.lower()