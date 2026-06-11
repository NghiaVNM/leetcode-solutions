class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
    return True if goal in s + s and len(s) == len(goal) else False