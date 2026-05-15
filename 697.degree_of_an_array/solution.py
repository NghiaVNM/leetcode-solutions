class Solution:
  def findShortestSubArray(self, nums: List[int]) -> int:
    first, count, degree, ans = {}, {}, 0, len(nums)

    for i, n in enumerate(nums):
      if n not in first:
        first[n] = i

      count[n] = count.get(n, 0) + 1

      if count[n] > degree:
        degree = count[n]
        ans = i - first[n] + 1
      elif count[n] == degree:
        ans = min(ans, i - first[n] + 1)

    return ans