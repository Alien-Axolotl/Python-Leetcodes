# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        traversal = list1

        list3 = ListNode(0)

        curr = list3

        while traversal is not None:
            curr.next = ListNode(traversal.val)
            curr = curr.next
            traversal = traversal.next

        traversal = list2   
        curr = list3 

        while traversal is not None:
            prev = list3
            while prev.next is not None and prev.next.val < traversal.val:
                prev = prev.next
            new_node = ListNode(traversal.val)
            new_node.next = prev.next
            prev.next = new_node
            traversal = traversal.next

        return list3.next        

                

            




                
        
