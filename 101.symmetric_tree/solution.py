class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]):
      if left is None and right is None:
        return True
      
      if left is None or right is None:
        return False
      
      if left.val != right.val:
        return False
      
      return isMirror(left.left, right.right) and isMirror(left.right, right.left)

    return isMirror(root.left, root.right)