class Solution:
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    ans = []
    def helper(_root: Optional[TreeNode], path):
      if _root == None: 
        return

      path += "->" + str(_root.val)

      if _root.left == _root.right == None:
        ans.append(path[2:])
        return

      helper(_root.left, path)
      helper(_root.right, path)
      return 

    helper(root, "")
    return ans