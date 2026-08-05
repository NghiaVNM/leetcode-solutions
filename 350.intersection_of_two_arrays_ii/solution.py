class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    for num in nums1:
      if num in nums2:
        ans.append(num)
        nums2 = nums2[:nums2.index(num)] + nums2[nums2.index(num) + 1:]

    return ans