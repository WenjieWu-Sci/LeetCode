# -*- coding: utf-8 -*-
# credit: https://www.jianshu.com/p/5875efe4748d

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


def CreateList(n):
    if n <= 0:
        return False
    if n == 1:
        return ListNode(1)
    else:
        root = ListNode(1)
        tmp = root
        for i in range(2, n+1):
            tmp.next = ListNode(1)
            tmp = tmp.next
    return root


def PrintList(head):
    p = head
    while p != None:
        print(p.val)
        p = p.next


def ListLen(head):
    c = 0
    p = head
    while p != None:
        c = c + 1
        p = p.next
    return c


def insert(head, n):
    if n < 1 or n > ListLen(head):
        return False
    p = head
    for i in range(1, n-1):
        p = p.next
    a = int(input('Enter a value : '))
    t = ListNode(a)
    t.next = p.next
    p.next = t
    return head


def dellist(head, n):
    if n < 1 or n > ListLen(head):
        return head
    elif n == 1:
        head = head.next
    else:
        p = head
        for i in range(1, n-1):
            p = p.next
        q = p.next
        p.next = q.next
    return head


def main():
    print('Create a linklist')
    head = CreateList(3)
    PrintList(head)
    print('------------------------')

    n1 = int(input('Enter the index to insert : '))
    insert(head, n1)
    PrintList(head)
    print('------------------------')
    
    n2 = int(input('Enter the index to delete : '))
    dellist(head, n2)
    PrintList(head)
    print('------------------------')


if __name__=='__main__':
    main()
