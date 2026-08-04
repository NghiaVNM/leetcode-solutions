class NumArray:
  arr = []
  def __init__(self, nums: List[int]):
    self.arr = nums

  def sumRange(self, left: int, right: int) -> int:
    return sum(self.arr[left : right+1])