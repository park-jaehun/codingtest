# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        result = []
        if not head:
            return True
        node = head
        while node is not None:
            result.append(node.val)
            node = node.next
        while len(result) > 1:
            if result.pop(0) != result.pop():
                return False

        return True

        """
        :type head: ListNode
        :rtype: bool
        """
