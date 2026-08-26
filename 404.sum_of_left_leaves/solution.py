class Solution:
  def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    def helper(_root: Optional[TreeNode]) -> int:
      if _root is None:
        return 0

      if _root.left is not None and _root.left.left is None and _root.left.right is None:
        return _root.left.val + helper(_root.right)

      return helper(_root.left) + helper(_root.right)

    return helper(root)