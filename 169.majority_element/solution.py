class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    _nums = dict(Counter(nums))

    for n, f in _nums.items():
      if f > len(nums) / 2:
        return n