class Solution:
  def shortestToChar(self, s: str, c: str) -> list[int]:
    n = len(s)
    answer = [0] * n

    prev = s.find(c)
    for j in range(prev):
      answer[j] = prev - j

    while True:
      nxt = s.find(c, prev + 1)
      if nxt == -1:
        break

      for j in range(prev + 1, nxt):
        answer[j] = min(j - prev, nxt - j)
      prev = nxt

    for j in range(prev + 1, n):
      answer[j] = j - prev

    return answer