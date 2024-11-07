def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    prev = ListNode(0)
        prev.next = head
        curr = prev

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
    
        return prev.next