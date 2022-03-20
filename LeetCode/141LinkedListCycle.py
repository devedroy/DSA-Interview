# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hashSet = set()
        # node = head
        # while node:
        #     if node in hashSet:
        #         return True
        #     hashSet.add(node)
        #     node = node.next
        # return False

        #Floyd's Tortoise and Hare
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False