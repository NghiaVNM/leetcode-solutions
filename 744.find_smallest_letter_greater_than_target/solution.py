class Solution:
  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    i = 0
    for letter in letters:
      if letter <= target:
        i += 1
    
    if i == len(letters):
      return letters[0]
    
    return letters[i]