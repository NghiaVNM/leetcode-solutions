class Solution:
  def toGoatLatin(self, sentence: str) -> str:
    words = sentence.split()
    ans = ""
    vowels = ["a", "o", "e", "u", "i"]

    for i in range(0, len(words)):
      if (words[i][0]).lower() not in vowels:
        words[i] = words[i][1:] + words[i][0]
      words[i] = words[i] + "ma"
      ans += " " + words[i] + (i + 1) * "a"

    return ans[1:]