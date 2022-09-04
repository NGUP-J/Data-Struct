class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkList:
    def __init__(self):
        self.head = self.tail = None
    
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
        return self.size() == 0

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
            return 0
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            node = Node(data)
            node.previous = current
            current.next = node
            self.tail = node

    def add_before(self, data):
        if self.isEmpty():
            self.head = self.tail = Node(data)
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

    def push_back(self, data):
        if self.isEmpty():
            self.head = self.tail = Node(data)
            return 0
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            node = Node(data)
            node.previous = current
            current.next = node
            self.tail = node

    def insert(self, index, data):
        if index > self.size() or index < 0:
            print('Data cannot be added')
            return
        if self.isEmpty():
            self.head = self.tail = Node(data)
            print(f'index = {index} and data = {data}')
            return 
        node = Node(data)

        if index == 0:
            self.add_before(data)
            print(f'index = {index} and data = {data}')
            return 

        if index == self.size():
            self.push_back(data)
            print(f'index = {index} and data = {data}')
            return

        current = self.head
        _index = 0
        while _index != index - 1:
            _index += 1
            current = current.next
        
        current.next.previous = node
        node.next = current.next
        node.previous = current
        current.next = node
        print(f'index = {index} and data = {data}')
        return

    def remove(self, data):
        if self.isEmpty():
            return print("Not Found!")
        current = self.head

        if self.size() == 1 and current.data == data:
            self.head = self.tail = None
            return print(f'removed : {data} from index : 0')

        if data == self.head.data:
            self.head = self.head.next
            self.head.previous = None
            return print(f'removed : {data} from index : 0')
        _index = 0

        while current.next is not None:
            if current.data == data:
                current.previous.next = current.next
                current.next.previous = current.previous
                return print(f'removed : {data} from index : {_index}')
            _index += 1
            current = current.next
        
        if current.data == data:
            self.tail = self.tail.previous
            self.tail.next = None
            return print(f'removed : {data} from index : {_index}')
        return print('Not Found!')

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

if __name__ == '__main__':
    Inp = input('Enter Input : ').split(',')

    L = LinkList()

    for a in Inp:
        a = a.split()
        if a[0] == 'A':
            L.append(a[1])
        elif a[0] == 'Ab':
            L.add_before(a[1])
        elif a[0] == 'I':
            index , data =  a[1].split(':')
            L.insert(int(index),data)
        elif a[0] == 'R':
            L.remove(a[1])
        print('linked list :',L)
        print('reverse :',L.str_reverse())