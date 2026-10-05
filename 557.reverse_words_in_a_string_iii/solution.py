class Solution:
  def reverseWords(self, s: str) -> str:
    ans = ""
    s = s.split()
    for e in s:
      ans += e[::-1] + " "
    
    return ans[:len(ans) - 1]