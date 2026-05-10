class Solution:
  def thirdMax(self, nums: List[int]) -> int:
    nums = sorted(list(set(nums)), reverse=True)
    if len(nums) <= 2:
      return nums[0]
    return nums[2]