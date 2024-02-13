class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
           
            first = current.next
            second = current.next.next
            
           
            first.next = second.next
            second.next = first
            current.next = second
            
       
            current = current.next.next
        
        return dummy.next
