class Solution:
  def reverseStr(self, s: str, k: int) -> str:
    res = []
    r = False
    
    for i in range(0, len(s), k):
      if not r:
        res.append(s[i:i+k][::-1])
      else: 
        res.append(s[i:i+k])
      r = not r
    return ''.join(res)