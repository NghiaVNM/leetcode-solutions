class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def height(_root: Optional[TreeNode]):
      if _root == None:
        return 0
      
      _left = height(_root.left)
      _right =  height(_root.right)

      if _left == -1 or _right == -1:
        return -1 
      
      if abs(_left - _right) > 1:
        return -1

      return 1 + max(_left, _right) 
    if height(root) == -1:
      return False
    return True