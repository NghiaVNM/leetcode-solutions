class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    total_sum = sum(nums)
    i = left_sum = 0

    while i < len(nums):
      if left_sum == total_sum - left_sum - nums[i]:
        return i
      left_sum += nums[i]
      i += 1

    return -1