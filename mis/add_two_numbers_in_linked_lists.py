#!/usr/bin/env python
# coding: utf-8

# 445. Add Two Numbers II
# Medium
# 
# 922
# 
# 123
# 
# Favorite
# 
# Share
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Success
# Details 
# Runtime: 84 ms, faster than 56.59% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 13.9 MB, less than 6.25% of Python3 online submissions for Add Two Numbers II.

# Could not time it as there are lots of interuption, but should be more than 30' and less than 1 hour.

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def get_len(l):
            n = 0
            while l != None:
                n += 1
                l = l.next
            return n
        n1, n2 = get_len(l1), get_len(l2)
        if n1 < n2:
            l1, l2 = l2, l1
            n1, n2 = n2, n1
        
        if n1 == 0:
            return ListNode(None)
        
        def addTwoLists(l1, l2, position = 0, result=None):
            position += 1
            if position == n1:
                tot = l1.val + l2.val
            elif position <= n1 - n2:
                result, carry = addTwoLists(l1.next, l2, position, result)
                tot = l1.val + carry
            else:
                result, carry = addTwoLists(l1.next, l2.next, position, result)
                tot = l1.val + l2.val + carry
            
            head = ListNode(tot % 10)
            head.next = result
            result = head
            carry = tot // 10
            return result, carry
        
        result, carry = addTwoLists(l1, l2)
        if carry == 1:
            head = ListNode(1)
            head.next = result
            result = head
        return result
            
        
            

