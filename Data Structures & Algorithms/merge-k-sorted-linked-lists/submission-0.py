# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge cases where lists are empty
        if not lists or len(lists) == 0:
            return None

        minHeap = []

        # Pushing first element from each list into minHeap
        for i, root in enumerate(lists):
            if root is not None:
                heapq.heappush(minHeap, (root.val, i, root))

        head, tail = None, None
        while minHeap:
            val, i, node = heapq.heappop(minHeap)

            # If this is the first node, initialize the head and the tail
            if not head:
                head, tail = node, node
            else:
                tail.next = node
                tail = tail.next

            if node.next is not None:
                heapq.heappush(minHeap, (node.next.val,i,  node.next))

        return head
