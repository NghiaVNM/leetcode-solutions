class Solution:
  def firstUniqChar(self, s: str) -> int:
    for chr in s:
      if s.count(chr) == 1:
        return s.index(chr)
    return -1