# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = (l1.val + l2.val) % 10
        rem = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next
        ret = ListNode(val)
        cur = ret
        while l1 != None or l2 != None:
            if l2 == None:
                while l1 != None:
                    s = l1.val + rem
                    val = s % 10
                    rem = s // 10
                    cur.next = ListNode(val)
                    cur = cur.next
                    l1 = l1.next
                    if l1 == None and rem != 0:
                        cur.next = ListNode(rem)
                        cur = cur.next
                return ret
            if l1 == None:
                while l2 != None:
                    s = l2.val + rem
                    val = s % 10
                    rem = s // 10
                    cur.next = ListNode(val)
                    cur = cur.next
                    l2 = l2.next
                    if l2 == None and rem != 0:
                        cur.next = ListNode(rem)
                        cur = cur.next
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
            