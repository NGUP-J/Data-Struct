class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkList:
    def __init__(self):
        self.head = self.tail = None
        self._size = 0
    
    def __str__(self):
        if self.isEmpty():
            return ''
        else:
            current, word = self.head, str(self.head.data)
            while current.next is not None:
                word += '->' + str(current.next.data)
                current = current.next
            return word
            
    def isEmpty(self):
        return self._size == 0

    def str_reverse(self):
        if self.isEmpty():
            return ''
        else:
            current, word = self.tail, str(self.tail.data)
            while current.previous is not None:
                word += '->' + str(current.previous.data)
                current = current.previous
            return word

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


    def insert(self, index, data):
        if index > self._size or index < 0:
            return print('Data cannot be added')

        if self.isEmpty():
            self.head = self.tail = Node(data)
            self._size += 1
            return print(f'index = {index} and data = {data}')
        node = Node(data)

        if index == 0:
            self._size += 1
            node.next = self.head
            self.head.previous = node
            self.head = node

        if index == self._size:
            self._size += 1
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        current, _index = self.head, 0

        while _index != index - 1:
            _index += 1
            current = current.next
        
        current.next.previous = node
        node.next = current.next
        node.previous = current
        current.next = node
        self._size += 1
        return print(f'index = {index} and data = {data}')

    def remove(self, data):
        if self.isEmpty():
            return print("Not Found!")
        current = self.head

        if self._size == 1 and current.data == data:
            self.head = self.tail = None
            self._size -= 1
            return print(f'removed : {data} from index : 0')
        self._size -= 1

        if data == self.head.data:
            self.head = self.head.next
            self.head.previous = None
            return print(f'removed : {data} from index : 0')
        _index = 0

        while current.next is not None:
            if current.data == data:
                current.previous.next = current.next
                current.next.previous = current.previous
                return print(f'removed : {data} from index : 0')
            _index += 1
            current = current.next
        
        if current.data == data:
            self.tail = self.tail.previous
            self.tail.next = None
            return print(f'removed : {data} from index : 0')
        self._size += 1
        return print('Not Found!')

    def size(self):
        return self._size

if __name__ == '__main__':
    Inp = input('Enter Input : ').split(',')

    L = LinkList()

    for a in Inp:
        a = a.split()
        if a[0] == 'A':
            L.append(a[1])
        elif a[0] == 'Ab':
            L.add_before(a[1])
            # L.insert(L.size() - 1, a[1])
        elif a[0] == 'I':
            L.insert(int(a[1].split(':')[0]),a[1].split(':')[1])
        elif a[0] == 'R':
            L.remove(a[1])
        print('linked list :',L)
        print('reverse :',L.str_reverse())