#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a new linked list
        head = ListNode(0)
        # set a pointer to the head of the list
        curr = head
        # set carry to 0
        carry = 0
        # while l1 or l2 or carry
        while l1 or l2 or carry:
            # if l1 is not None
            if l1:
                # add l1.val to carry
                carry += l1.val
                # set l1 to l1.next
                l1 = l1.next
            # if l2 is not None
            if l2:
                # add l2.val to carry
                carry += l2.val
                # set l2 to l2.next
                l2 = l2.next
            # set curr.next to ListNode(carry % 10)
            curr.next = ListNode(carry % 10)
            # set curr to curr.next
            curr = curr.next
            # set carry to carry // 10
            carry = carry // 10
        # return head.next
        return head.next

        
# @lc code=end

