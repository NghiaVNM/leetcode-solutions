class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    tmp = set()
    for i in range(len(nums)):
      if nums[i] in tmp:
        return True
      tmp.add(nums[i])
      if len(tmp) > k:
        tmp.remove(nums[i - k])
    return False