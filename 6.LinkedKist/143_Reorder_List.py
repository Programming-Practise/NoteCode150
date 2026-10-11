# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        mid_head = slow
        last_linked_list = self.reverseList(mid_head)
        
        dummy = ListNode(0)
        cur = dummy
        cur_left = head
        cur_right = last_linked_list
        while cur_left != slow:
            cur.next = cur_left
            cur = cur.next
            cur_left = cur_left.next
            cur.next = cur_right
            cur = cur.next
            cur_right = cur_right.next
        cur.next = slow
        return dummy



    def reverseList(self, head: ListNode | None) -> None:
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre