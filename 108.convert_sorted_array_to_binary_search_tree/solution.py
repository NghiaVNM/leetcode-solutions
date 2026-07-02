class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:  
    if nums == []:
      return None
      
    root = TreeNode(nums[len(nums) // 2])
    root.left = self.sortedArrayToBST(nums[:len(nums) // 2])
    root.right = self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
    
    return root