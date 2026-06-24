class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    stack = []
    ans = []
    cur = root

    while cur is not None or stack:
      while cur is not None:
        stack.append(cur)
        cur = cur.left

      cur = stack.pop()
      ans.append(cur.val)

      cur = cur.right

    return ans