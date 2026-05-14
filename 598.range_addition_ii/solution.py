class Solution:
  def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    if(len(ops)) == 0:
      return m * n
    min_m = float('inf')
    min_n = float('inf')
    for i in range(len(ops)):
      if ops[i][0] < min_m:
        min_m = ops[i][0]
    for i in range(len(ops)):
      if ops[i][1] < min_n:
        min_n = ops[i][1]
    return min_m * min_n