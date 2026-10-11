
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy = Node()

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        cur = self.dummy.next

        while index > 0 and cur:
            cur = cur.next
            index -= 1

        return cur.val if cur else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node

    def addAtTail(self, val: int) -> None:
        cur = self.dummy

        while cur.next:
            cur = cur.next

        cur.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        cur = self.dummy

        while index > 0 and cur:
            cur = cur.next
            index -= 1

        if cur is None:
            return

        new_node = Node(val)
        new_node.next = cur.next
        cur.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        cur = self.dummy

        while index > 0 and cur.next:
            cur = cur.next
            index -= 1

        if index == 0 and cur.next:
            cur.next = cur.next.next
