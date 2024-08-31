# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0

        i = 0
        acc = 0
        while l1:
            acc += l1.val*10**i
            i+=1
            l1 = l1.next

        i = 0
        while l2:
            acc += l2.val*10**i
            i+=1
            l2 = l2.next

        root = None
        str_acc = str(acc)        
        for s in str_acc: # 앞에 붙이면서 reverse
            new_node = ListNode(int(s))
            if not root:
                root = new_node
                continue

            new_node.next = root
            root = new_node

        return root
