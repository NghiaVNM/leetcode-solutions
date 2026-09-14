class Solution:
  def constructRectangle(self, area: int) -> List[int]:
    tmp = math.floor(area ** 0.5)
    while tmp > 1:
      if area % tmp == 0:
        return [int(area / tmp), tmp]
      tmp -= 1

    return [area, 1]