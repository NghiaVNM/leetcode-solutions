class Solution:
  def uniqueMorseRepresentations(self, words: List[str]) -> int:
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    tmp = set()

    for word in words:
      word_morse = ""
      for char in word:
        word_morse += morse[ord(char) - 97]
      tmp.add(word_morse)

    return len(tmp)