class Solution:
  def reverseVowels(self, s: str) -> str:
    vols = set('aeiouAEIOU')
    arr = list(s)
    left, right = 0, len(arr) - 1
    while left < right:
      while left < right and arr[left] not in vols:
        left += 1
      while left < right and arr[right] not in vols:
        right -= 1
      if left < right:
        arr[left], arr[right] = arr[right], arr[left]
      left += 1
      right -= 1
    return ''.join(arr)