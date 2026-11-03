class Solution:
  def dominantIndex(self, nums: list[int]) -> int:
    _max = max(nums)

    for n in nums:
      if n == _max:
        continue

      if n * 2 > _max:
        return -1
    return nums.index(_max)
  