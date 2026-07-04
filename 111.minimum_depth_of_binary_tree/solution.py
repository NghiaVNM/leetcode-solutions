class Solution:
  def minDepth(self, root: Optional[TreeNode]) -> int:
    if root == None:
      return 0

    if root.left == None and root.right == None:
      return 1
    
    if root.left != None and root.right != None:
      return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    
    if root.left != None:
      return self.minDepth(root.left) + 1
    else:
      return self.minDepth(root.right) + 1