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
            val, index = heapq.heappop(min_heap)
            current_node.next = lists[index]
            current_node = current_node.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(min_heap, (lists[index].val, index))

        return temp_node.next