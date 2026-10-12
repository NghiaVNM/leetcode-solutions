class Solution:
  def judgeCircle(self, moves: str) -> bool:
    left_move = moves.count('L')
    right_move = moves.count('R')
    up_move = moves.count('U')
    down_move = moves.count('D')

    if left_move != right_move or up_move != down_move:
      return False
    return True