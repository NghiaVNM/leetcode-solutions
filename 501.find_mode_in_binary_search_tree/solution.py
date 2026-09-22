class Solution:
  def findMode(self, root: TreeNode | None) -> list[int]:
    ans = []
    _max = 0
    count = 0
    prev = None

    def inorder(root):
      nonlocal prev, count, _max, ans

      if root is None:
        return

      inorder(root.left)

      if prev is None or root.val != prev:
        count = 1
      else:
        count += 1

      if count > _max:
        _max = count
        ans = [root.val]
      elif count == _max:
        ans.append(root.val)

      prev = root.val

      inorder(root.right)

    inorder(root)

    return ans