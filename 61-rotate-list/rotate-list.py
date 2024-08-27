# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """      
        if not head or not k: 
            return head
        
        last_element, temp_list = head, 1
        while last_element.next:
            last_element = last_element.next
            temp_list += 1
            
        last_element.next = head
        for _ in range(temp_list - k % temp_list):
            last_element = last_element.next
            
        final_list = last_element.next
        last_element.next = None
        
        return final_list