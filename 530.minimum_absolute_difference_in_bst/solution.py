class Solution:
  def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    min_diff = float('inf')
    prev = None

    def traverse(node):
      nonlocal min_diff, prev

      if node is None:
        return

      traverse(node.left)

      if prev is not None:
        min_diff = min(min_diff, abs(prev - node.val))

      prev = node.val

      traverse(node.right)     

    traverse(root)
    return min_diff   