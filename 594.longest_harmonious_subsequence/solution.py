class Solution:
  def findLHS(self, nums: List[int]) -> int:
    freq = {}
    for num in nums:
      if num not in freq:
        freq[num] = 1
      else:
        freq[num] += 1

    _max = 0
    for num in freq:
      if num + 1 in freq:
        if freq[num] + freq[num + 1] > _max:
          _max = freq[num] + freq[num + 1]
        
    return _max