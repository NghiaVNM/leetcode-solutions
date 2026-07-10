class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ans = []

    def helper(_root: Optional[TreeNode]):
      if _root == None:
        return 
      
      ans.append(_root.val)
      
      helper(_root.left)
      helper(_root.right)
    
    helper(root)
    return ans