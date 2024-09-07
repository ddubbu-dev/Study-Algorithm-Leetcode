# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
[분석]
- root : Complete BT
- return: depth가 1씩 증가하는지

[주의 사항]
- input LinkedList, Tree 형태
- BST 아님, 완전탐색해야함
- 노드 value 중복 가능 : left, right 각각 탐색 필요함

[힌트]
- 재귀를 어떤함수로 돌지, subproblem 발견이 중요함

"""
import math

class Solution:
    def find(self,  head: Optional[ListNode], root: Optional[TreeNode])->bool:
        if head == None: # 탈출 - 탐색 완료
            return True
        elif root == None: # 탈출 - 다음 path 없음
            return False

        if root.val == head.val:
            return self.find(head.next, root.left) or self.find(head.next, root.right)
            
        return False

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        return self.find(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

