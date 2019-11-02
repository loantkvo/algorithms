#!/usr/bin/env python
# coding: utf-8

# https://leetcode.com/problems/add-one-row-to-tree/
# 
# 623. Add One Row to Tree
# Medium
# 
# 330
# 
# 112
# 
# Favorite
# 
# Share
# Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.
# 
# The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.
# 
# Example 1:
# 
# Input: 
# A binary tree as following:
#        4
#      /   \
#     2     6
#    / \   / 
#   3   1 5   
# 
# v = 1
# 
# d = 2
# 
# Output: 
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     / 
#  3   1   5   
# 
# Example 2:
# 
# Input: 
# A binary tree as following:
#       4
#      /   
#     2    
#    / \   
#   3   1    
# 
# v = 1
# 
# d = 3
# 
# Output: 
#       4
#      /   
#     2
#    / \    
#   1   1
#  /     \  
# 3       1
# Note:
# 
# The given d is in range [1, maximum depth of the given tree + 1].
# The given binary tree has at least one tree node.
# 

# Success
# Details 
# Runtime: 56 ms, faster than 84.06% of Python3 online submissions for Add One Row to Tree.
# Memory Usage: 17.6 MB, less than 25.00% of Python3 online submissions for Add One Row to Tree.

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def insert_row(ancestor, depth):
            if depth == 1:
                newNode_left = TreeNode(v)
                newNode_left.left = ancestor.left
                ancestor.left = newNode_left
                
                newNode_right = TreeNode(v)
                newNode_right.right = ancestor.right
                ancestor.right = newNode_right
            else:
                if ancestor.left != None:
                    ancestor.left = insert_row(ancestor.left, depth-1)
                if ancestor.right != None:
                    ancestor.right = insert_row(ancestor.right, depth-1)
            return ancestor
        
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            root = new_root
            return root
        else: # d > 1
            root = insert_row(root, d-1)
        return root
            
        
        
        


# In[ ]:





# In[ ]:




