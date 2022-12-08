# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''
>>> s = Solution()
>>> s.addTwoNumbers([2,4,3], [5,6,4])
[7,0,8]
>>> s = Solution()
>>> s.addTwoNumbers([0], [0])
[0]
>>> s = Solution()
>>> s.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])
[8,9,9,9,0,0,0,1]
'''


# Definition for singly-linked list.
from ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        l4 = l3

        while l1 != None and l2 != None:
            div = int((l3.val + l1.val + l2.val) // 10)
            l3.val = (l3.val + l1.val + l2.val) % 10
            if l1.next != None or l2.next != None or div >= 1:
                l3.next = ListNode() 
                l3.next.val = div
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
                

        while l1 != None:
            div = int((l3.val + l1.val) // 10)
            l3.val = (l3.val + l1.val) % 10
            if l1.next != None or div >= 1:
                l3.next = ListNode() 
                l3.next.val = div
            l1 = l1.next
            l3 = l3.next


        while l2 != None:
            div = int((l3.val + l2.val) // 10)
            l3.val = (l3.val + l2.val) % 10
            if l2.next != None or div >= 1:
                l3.next = ListNode() 
                l3.next.val = div
            l2 = l2.next
            l3 = l3.next

        return l4

if __name__ == '__main__':
    import doctest
    doctest.testmod()