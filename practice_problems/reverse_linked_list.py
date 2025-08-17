from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        # curr = head
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            print(f"prev: {prev.val}")

        return prev

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    sol = Solution()
    sol.reverseList(head)


main()
