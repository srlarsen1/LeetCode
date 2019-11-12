# https://leetcode.com/problems/remove-linked-list-elements/

# Remove all elements from a linked list of integers that have value val.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head != None and head.val == val:
            head = head.next    
        current = head
        while current != None:
            if current.next and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head