class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    nums2_len = len(nums2) - 1
    for num in nums1:
      idx = nums2.index(num)
      for i in range(idx + 1, nums2_len + 1):
        if nums2[i] > num:
          ans.append(nums2[i])
          break
      else:
        ans.append(-1)
    return ans