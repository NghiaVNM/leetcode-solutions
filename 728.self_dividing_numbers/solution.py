class Solution:
  def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    ans = []

    for i in range(left, right + 1):
      tmp = str(i)

      if '0' in tmp:
        continue
      
      for digit in tmp:
        if i % int(digit) != 0:
          break
      else:
        ans.append(i)
        
    return ans