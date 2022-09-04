class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, head = None):
        self.head = self.tail = None
        self._size = 0
    
    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        else:
            current, word = self.head, str(self.head.data)
            while current.next is not None:
                word += ' -> ' + str(current.next.data)
                current = current.next
            return word
            
    def isEmpty(self):
        return self.size() == 0

    def append(self, data):
        if self.isEmpty():
            self.head = self.tail = Node(data)
            self._size += 1
            return 0
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            node = Node(data)
            node.previous = current
            current.next = node
            self.tail = node
            self._size += 1

    def add_before(self, data):
        if self.isEmpty():
            self.head = self.tail = Node(data)
            self._size += 1
            return 0
        else:
            node = Node(data)
            if self.size() == 1:
                node.next = self.tail
                self.tail.previous = node
                self.head = node
            else:
                node.next = self.head
                self.head.previous = node
                self.head = node
            self._size += 1

    def push_back(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def remove(self):
        temp = self.head.data
        self.head = self.head.next 
        temp = int(temp)
        return temp

    def peek(self):
        return self.head.data

def get_digit(n, d):
    for i in range(d-1):
        n //= 10
    return n % 10

def get_max_digit(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

def radix_sort(l, st):
    node = l
    max_bits = get_max_digit(max([int(abs(a)) for a in st]))
    n = [LinkedList(), LinkedList(), LinkedList(), LinkedList(), LinkedList(),
         LinkedList(), LinkedList(), LinkedList(), LinkedList(), LinkedList()]
    count = 0
    for i in range(1, max_bits+2):
        print('------------------------------------------------------------')
        print(f'Round : {i}')
        count += 1
        while not node.isEmpty():
            num = int(node.remove())
            if num < 0:
                index_digit = get_digit(num*-1, i)
            else:
                index_digit = get_digit(num, i)
            n[index_digit].add_before(num)
        countn = 0
        for i in range(10):
            print(f'{i} : ', end='')
            flag = sort(n[i])
            if i != 0 and n[i].isEmpty():
                countn += 1
            while not n[i].isEmpty():
                print(n[i].peek(), end = ' ')
                node.push_back(n[i].remove())
            print()
            if countn == 9:
                flag = False
        if flag is False:
            break
    print('------------------------------------------------------------')
    print(f'{count - 1} Time(s)')
    return node.head

def sort(node):
    
    if not node.isEmpty():
        i = 0
        while i < node.size():
            itr = node.head
            j = 0
            while j < node.size() and itr.next:
                if itr.data < itr.next.data:
                    itr.data, itr.next.data = itr.next.data, itr.data
                itr = itr.next
                j += 1
            i += 1
    count = 0

if __name__ == '__main__':
    inp = [int(a) for a in input('Enter Input : ').split(' ')]
    lbefore = LinkedList()
    lafter = LinkedList()

    for i in inp:
        lbefore.append(int(i))
        lafter.append(int(i))

    radix_sort(lafter, inp)
    print(f'Before Radix Sort : {lbefore}')
    print(f'After  Radix Sort : {lafter}')