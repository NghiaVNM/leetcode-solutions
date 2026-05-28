class Solution:
  def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])

    if m * n != r * c:
      return mat
    
    ans = []

    for i in range(r):
      row = []
      for j in range(c):
        index = i * c + j
        row.append(mat[index // n][index % n])
      ans.append(row)

    return ans