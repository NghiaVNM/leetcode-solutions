class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def helper(_root: Optional[TreeNode], curSum: int) -> bool:
      if _root == None:
        return False
        
      if (_root.left == None and _root.right == None):
        if _root.val + curSum == targetSum:
          return True
        else:
          return False
        
      return helper(_root.left, _root.val + curSum) or helper(_root.right, _root.val + curSum)
    
    return helper(root, 0)