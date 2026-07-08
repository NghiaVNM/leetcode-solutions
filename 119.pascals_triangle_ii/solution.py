class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    cur = [1, 1]
    pre = [1]

    if rowIndex == 0:
      return pre
    if rowIndex == 1:
      return cur
    
    i = 2
    while i <= rowIndex:
      pre = cur
      cur = []
      cur.append(1)
      for j in range(len(pre) - 1):
        cur.append(pre[j] + pre[j + 1])
      cur.append(1)
      i += 1
      
    return cur