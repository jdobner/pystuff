# Definition for a binary tree node.
from typing import List, Optional

def test():
    node = TreeNode(-2, None, TreeNode(-3))
    s = Solution()
    print(s.pathSum(node, -5))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode({self.val}, {self.left}, {self.right})"


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.rv = []
        self.target = targetSum
        self.search(root, 0, [])
        return self.rv
        
    def search(self, node: TreeNode, val, path: List[int]):
        # print("check", node, val, path)
        if node is None:
            return
        newval = val + node.val
        path.append(node.val)
        if newval == self.target and node.left is None and node.right is None:
            self.rv.append(path)
        self.search(node.left, newval, list(path))
        self.search(node.right, newval, list(path))

if __name__ == '__main__':
    test()
