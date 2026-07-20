

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            num1 = 0
            num2 = 0

            if l1:
                num1 = l1.val
                l1 = l1.next

            if l2:
                num2 = l2.val
                l2 = l2.next

            total = num1 + num2 + carry

            carry = total // 10

            current.next = ListNode(total % 10)

            current = current.next

        return dummy.next