
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)

        digitsl1 = -1
        digitsl2 = -1
        numberl1 = 0
        numberl2 = 0

        while l1 is not None:
            digitsl1 = digitsl1 + 1
            numberl1 = numberl1 + l1.val*(10**digitsl1)
            l1 = l1.next
        while l2 is not None:
            digitsl2 = digitsl2 + 1
            numberl2 = numberl2 + l2.val*(10**digitsl2)
            l2 = l2.next

        numberl3 = numberl1 + numberl2

        current = dummyHead

        while numberl3 is not 0:

            current.next = ListNode(0)
            current = current.next
            current.val = numberl3 % 10
            numberl3 = numberl3 // 10

        if dummyHead.next is None:
            return ListNode(0)    


        return dummyHead.next    

