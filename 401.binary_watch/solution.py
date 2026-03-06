class Solution:
  def readBinaryWatch(self, turnedOn: int) -> List[str]:
    ans = []
    for h in range(12):
      for m in range(60):
        if bin(h).count('1') + bin(m).count('1') == turnedOn:
          if m < 10:
            m = '0' + str(m)
          ans.append(str(h) + ":" + str(m))
    return ans