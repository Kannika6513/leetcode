class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # Store next node
            curr.next = prev        # Reverse the link
            prev = curr             # Move prev forward
            curr = next_node        # Move curr forward

        return prev