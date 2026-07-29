class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    ranges = []

    if len(nums) == 0:
      return ranges

    start = nums[0]
    end = nums[0]
    for i in range(len(nums) - 1):
      if nums[i + 1] - nums[i] != 1:
        if start == end:
          _range = str(start)
        else:
          _range = str(start) + "->" + str(end)
        ranges.append(_range)
        start = end = nums[i + 1]
      else:
        end = nums[i + 1]

    if start == end:
      _range = str(start)
    else:
      _range = str(start) + "->" + str(end)
    ranges.append(_range)

    return ranges