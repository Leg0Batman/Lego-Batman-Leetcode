class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
             return root.right
            elif not root.right:
             return root.left
            
            min_larger_node = self.getMin(root.right)
            root.val = min_larger_node.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root

    def getMin(self, node: TreeNode) -> TreeNode:
     while node.left:
            node = node.left
     return node