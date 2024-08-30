# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))

        temp_node = ListNode(0)
        current_node = temp_node
        
        while min_heap:
            val, list_index = heapq.heappop(min_heap)
            current_node.next = lists[list_index]
            current_node = current_node.next
            lists[list_index] = lists[list_index].next
            if lists[list_index]:
                heapq.heappush(min_heap, (lists[list_index].val, list_index))

        return temp_node.next