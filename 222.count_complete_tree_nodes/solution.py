class Solution:
  def countNodes(self, root: Optional[TreeNode]) -> int:
    if root == None:
      return 0

    def getHeight(node: Optional[TreeNode]):
      if node == None:
        return 0
      
      return 1 + getHeight(node.left)
    
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)
    if left_height == right_height:
      return (1 << left_height) + self.countNodes(root.right)
    return (1 << right_height) + self.countNodes(root.left)