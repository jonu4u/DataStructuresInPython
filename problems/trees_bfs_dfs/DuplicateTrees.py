# 652. Find Duplicate Subtrees
#
# Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with the same node values.
#
# Example 1:
#
#
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# Example 2:
#
#
# Input: root = [2,1,1]
# Output: [[1]]
# Example 3:
#
#
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
#
#
# Constraints:
#
# The number of the nodes in the tree will be in the range [1, 10^4]
# -200 <= Node.val <= 200


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        # The approach here is we serialize the tree and at each step we store the serialized value
        dup_map={}
        ans=[]
        def lookup(root):
            if not root: return '#'
            # At each iteration the subtree is rootvalue+leftval+rightval
            subtree='{},{},{}'.format(root.val,lookup(root.left),lookup(root.right))
            # We store this subtree in the map and increase count by 1
            dup_map[subtree]=dup_map.get(subtree,0)+1
            # When the subtree is 2 we add to ans the parent node ofthe subtree
            if dup_map[subtree]==2:
                ans.append(root)
            return subtree
        lookup(root)
        return ans