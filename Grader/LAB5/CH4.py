class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self._size = 0
    
    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        else:
            current, word = self.head, str(self.head.data)
            while current.next is not None:
                word += '->' + str(current.next.data)
                current = current.next
            return word
            
    def isEmpty(self):
        return self._size == 0

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

    def redirect(self, index1, index2):
        if index1 == 0 and index2 == 0 and self.isEmpty():
            return
        elif not 0 <= index1 < self.size():
            print(f'Error! {{index not in length}}: {index1}')
        elif not 0 <= index2 < self.size():
            print(f'index not in length, append : {index2}')
            self.push_back(index2)
        else:
            current = self.head
            count = 0
            while current is not None and count < index1:
                current = current.next
                count += 1
            node1 = current
            current = self.head
            count = 0
            while current is not None and count < index2:
                current = current.next
                count += 1
            node2 = current
            node1.next = node2
            node2.previous = node1
            print(f'Set node.next complete!, index:value = {index1}:{node1.data} -> {index2}:{node2.data}')

    def detectLoop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False

if __name__ == '__main__':
    inp = input('Enter input : ').split(',')
    l = LinkedList()

    for i in inp:
        if 'A' in i:
            l.append(i[2:])
            print(l)
        elif 'S' in i:
            ind1 ,ind2 = i[2:].split(':')
            if l.isEmpty():
                print('Error! {list is empty}')
            else:
                l.redirect(int(ind1), int(ind2))
    if l.detectLoop():
        print('Found Loop')
    else:
        print('No Loop')
        print(l)