from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        ans = []
        q = deque([root])
        
        while q:
            level_size = len(q)
            level_sum = 0

            for _ in range(level_size):
                curr = q.popleft()
                level_sum += curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            ans.append(level_sum / level_size)    

        return ans