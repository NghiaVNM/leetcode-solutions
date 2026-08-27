class Solution:
  def longestPalindrome(self, s: str) -> int:
    ans = 0
    flag = False

    freq_dict = defaultdict(int)
    for ele in s:
      freq_dict[ele] += 1
    res = freq_dict.items()

    for i in res:
      if i[1] == 1 and not flag:
        ans += 1
        flag = True

      if i[1] % 2 == 0:
        ans += i[1]
      elif not flag:
        ans += i[1]
        flag = True
      else:
        ans += i[1] - 1

    return ans