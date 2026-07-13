class Solution:
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ans = []

    def helper(_root: Optional[TreeNode]):
      if _root == None:
        return
    
      helper(_root.left)
      helper(_root.right)
      ans.append(_root.val)

    helper(root)
    return ans