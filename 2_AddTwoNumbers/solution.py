# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    ans = ListNode(0)
    tmp = ans
    tmpsum = 0
    while True:
        if l1 != None:
            tmpsum += l1.val
            l1 = l1.next
        if l2 != None:
            tmpsum += l2.val
            l2 = l2.next
        tmp.val = tmpsum % 10
        tmpsum //= 10
        if l1 == None and l2 == None and tmpsum == 0:
            break
        tmp.next = ListNode(0)
        tmp = tmp.next
    return ans


def main():
    l1 = ListNode(2)
    tmp = l1
    tmp.next = ListNode(4)
    tmp = tmp.next
    tmp.next = ListNode(3)

    l2 = ListNode(5)
    tmp = l2
    tmp.next = ListNode(6)
    tmp = tmp.next
    tmp.next = ListNode(4)

    l3 = addTwoNumbers(l1, l2)
    print(l3.val)
    l3 = l3.next
    print(l3.val)
    l3 = l3.next
    print(l3.val)


if __name__=='__main__':
    main()


#def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#    carry = 0
#    root = n = ListNode(0)
#    while l1 or l2 or carry:
#        v1 = v2 = 0
#        if l1:
#            v1 = l1.val
#            l1 = l1.next
#        if l2:
#            v2 = l2.val
#            l2 = l2.next
#        carry, val = divmod(v1+v2+carry, 10)
#        n.next = ListNode(val)
#        n = n.next
#    return root.next
