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
        if not head:
            return None
        
        last_element = head
        list_length = 1

        while ( last_element.next ):
            last_element = last_element.next
            list_length += 1

        k = k % list_length
            
        last_element.next = head
        
        temp_node = head
        for _ in range(list_length - k - 1 ):
            temp_node = temp_node.next

        final_list = temp_node.next
        temp_node.next = None
        
        return final_list