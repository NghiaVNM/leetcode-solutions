class Solution:
  def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
    rows = len(img)
    cols = len(img[0])

    ans = [[0] * cols for _ in range (rows)]

    for row in range(rows):
      for col in range(cols):
        total = 0
        count = 0
        for r in range(row - 1, row + 2):
          for c in range(col - 1, col + 2):
            if r in range(rows) and c in range(cols):
              total += img[r][c]
              count += 1
        ans[row][col] = total // count

    return ans