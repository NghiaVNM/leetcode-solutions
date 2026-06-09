class Solution:
  def findErrorNums(self, nums: List[int]) -> List[int]:
    dup = -1

    for num in nums:
      i = abs(num) - 1
      if nums[i] < 0:
        dup = abs(num)
      else:
        nums[i] = -nums[i]

    missing = -1
    for i, num in enumerate(nums):
      if num > 0:
        missing = i + 1
        break

    return [dup, missing]