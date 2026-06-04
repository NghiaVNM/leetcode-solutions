class Solution:
  def largestTriangleArea(self, points: List[List[int]]) -> float:
    _max = 0
    for i in range(len(points) - 2):
      for j in range(i + 1, len(points) - 1):
        for z in range(j + 1, len(points)):
          area = abs(points[i][0] * (points[j][1] - points[z][1]) + points[j][0] * (points[z][1] - points[i][1]) + points[z][0] * (points[i][1] - points[j][1])) * 0.5
          if area > _max:
            _max = area

    return _max