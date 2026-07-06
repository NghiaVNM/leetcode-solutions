class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    ans = []
    i = 1
    
    while i <= numRows:
      if i == 1:
        ans.append([1])
      elif i == 2:
        ans.append([1, 1])
      else:
        tmp = []
        tmp.append(1)
        for j in range(len(ans[i - 2]) - 1):
          tmp.append(ans[i - 2][j] + ans[i - 2][j + 1])
        tmp.append(1)
        ans.append(tmp)
      i += 1
    
    return ans