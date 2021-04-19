# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def fill(self, cur, lx, rem):
        while lx != None:
            s = lx.val + rem
            val = s % 10
            rem = s // 10
            cur.next = ListNode(val)
            cur = cur.next
            lx = lx.next
            if lx == None and rem != 0:
                cur.next = ListNode(rem)
                cur = cur.next
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = l1.val + l2.val
        val = s  % 10
        rem = s // 10
        l1 = l1.next
        l2 = l2.next
        ret = ListNode(val)
        cur = ret
        while l1 != None or l2 != None:
            if l2 == None:
                self.fill(cur, l1, rem)
                return ret
            if l1 == None:
                self.fill(cur, l2, rem)
                return ret
            
            s = l1.val + l2.val + rem
            val = s % 10
            rem = s // 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
            
        if rem != 0:
            cur.next = ListNode(rem)
            cur = cur.next
        return ret
