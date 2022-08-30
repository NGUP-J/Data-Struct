class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
class LinkedList:

    def __init__(self):
        self.head = self.tail =  None
        self._size = 0

    def __str__(self):
        return str(self.head)

    def printList(self): # print list
        if self.isEmpty():
            print("List is empty")
        else:
            itr = self.head
            output = ''
            while itr:
                output += str(itr.data)
                if itr.next is not None:
                    output += "->"
                itr = itr.next
            print("link list :",output)

    def isEmpty(self):  # listedlist is empty
        return self._size == 0
    
    def append(self, data): # add data to link list
        self._size += 1
        node = Node(data, None)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def insert(self, index, data): # insert data to link list
        node = Node(data)

        if (index < 0 or index > self._size):
            return print("Data cannot be added")
        elif (index == 0):
            self._size += 1
            node.next = self.head
            self.head = node
            return print(f'index = {index} and data = {data}')
        else:
            current = self.head
            for i in range(0, index - 1):
                if (current != None):
                    current = current.next
            if (current != None):
                self._size += 1 
                node.next = current.next
                current.next = node
                return print(f'index = {index} and data = {data}')
            else:
                self._size += 1
                current = self.head
                while(current.next != None):
                    current = current.next
                current.next = node
                return print(f'index = {index} and data = {data}')

    def size(self): # return size of link list
        return self._size

if __name__ == '__main__':
    inp = input("Enter Input : ").split(',')
    l = LinkedList()
    for i in inp:
        if ':' not in i: # add node
            if i != "":
                data = i.split(' ')
                for i in data:
                    l.append(i)
                intr = l.head
        else:   # insert to link list
            ins = i.split(':')
            l.insert(int(ins[0].lstrip()), ins[1])
        l.printList()
        # print("size :", l.size())
