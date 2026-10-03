# 要实现链表反转，需要三个指针，cur当前node,pre是前一个node,temp是后一个node
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        cur = head
        pre = None
        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre

