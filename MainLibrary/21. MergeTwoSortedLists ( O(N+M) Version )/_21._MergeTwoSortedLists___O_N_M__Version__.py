# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        list3 = ListNode(0)

        curr = list3

        traversal1 = list1
        traversal2 = list2

        while traversal1 is not None and traversal2 is not None:

            if traversal1.val <= traversal2.val:
                curr.next = traversal1      
                traversal1 = traversal1.next  
            else:
                curr.next = traversal2       
                traversal2 = traversal2.next  
            
            curr = curr.next
            
        while traversal1 is not None:
            curr.next = ListNode(traversal1.val)
            traversal1 = traversal1.next
            curr = curr.next

        while traversal2 is not None:
            curr.next = ListNode(traversal2.val)
            traversal2 = traversal2.next
            curr = curr.next    

        return list3.next    
            



                

            




                
        
