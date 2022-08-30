class node:
    def __init__(self,data,next = None ):
        ### Code Here ###
        self.data = data
        self.next = next
    def __str__(self):
        ### Code Here ###
        return self.data

def createList(l=[]):
    Head = None
    for num in l:
        if Head is None:
            Head = node(int(num))
        else:
            current = Head
            while current.next:
                current = current.next
            current.next = node(int(num))
    return Head
    ### Code Here ###

def printList(H):
    ### Code Here ###
    current = H
    while current:
        print(current.data, end =' ')
        current = current.next
    print()

def mergeSort(p):
    if (p.next == None):
        return p
    mid = findMid(p)
    head2 = mid.next
    mid.next = None
    newHead1 = mergeSort(p)
    newHead2 = mergeSort(head2)

    merged = node(0)

    temp = merged

    while (newHead1 != None and newHead2 != None):
        if (newHead1.data < newHead2.data):
            temp.next = newHead1
            newHead1 = newHead1.next
        else:
            temp.next = newHead2
            newHead2 = newHead2.next
        temp = temp.next
      
    while (newHead1 != None):
        temp.next = newHead1
        newHead1 = newHead1.next
        temp = temp.next
      
    while (newHead2 != None):
        temp.next = newHead2
        newHead2 = newHead2.next
        temp = temp.next

    return merged.next

def mergeOrderesList(p,q):
    ## Code Here ###
    itr = p
    while itr.next:
        itr = itr.next
    temp = q
    while temp:
        itr.next = node(temp.data, itr.next)
        temp = temp.next
        itr = itr.next
    finalHead = mergeSort(p)
    return finalHead

def findMid(head):
    slow = head
    fast = head.next
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == '__main__':
    inp1, inp2 = input('Enter 2 Lists : ').split(' ')
    L1 = inp1.split(',')
    L2 = inp2.split(',')
    #################### FIX comand ####################   
    # input only a number save in L1,L2
    LL1 = createList(L1)
    LL2 = createList(L2)
    print('LL1 : ',end='')
    printList(LL1)
    print('LL2 : ',end='')
    printList(LL2)
    m = mergeOrderesList(LL1,LL2)
    print('Merge Result : ',end='')
    printList(m)