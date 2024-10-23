from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_view = []
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()
            if level == len(right_view):
                right_view.append(node.val)
            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))

        return right_view