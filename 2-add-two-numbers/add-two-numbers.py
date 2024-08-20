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
        initial = ListNode()
        solution = initial

        total = remainder = 0

        while l1 or l2 or remainder:
            total = remainder

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            number = total % 10
            remainder = total // 10
            initial.next = ListNode(number)
            initial = initial.next
        
        return solution.next