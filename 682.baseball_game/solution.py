class Solution:
  def calPoints(self, operations: List[str]) -> int:
    ans = []
    for ops in operations:
      if ops == "+":
        ans.append(int(ans[len(ans) - 1]) + int(ans[len(ans) - 2]))
      elif ops == "D":
        ans.append(int(ans[len(ans) - 1]) * 2)
      elif ops == "C":
        ans.pop()
      else:
        ans.append(int(ops))
    return sum(ans)