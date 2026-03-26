class Solution:
  def findRelativeRanks(self, score: List[int]) -> List[str]:
    ans = [''] * len(score)
    medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']

    for rank, (idx, s) in enumerate(sorted(enumerate(score), key=lambda x: -x[1])):
      ans[idx] = medals[rank] if rank < 3 else str(rank + 1)

    return ans