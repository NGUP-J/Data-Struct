class node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
class LinkList:

    def __str__(self):
        return str(self.data)
    def __init__(self):
        self.head = self.tail =  None
        self._size = 0

    def __str__(self):
        return str(self.head)

    def isEmpty(self):
        return self._size == 0
    
    def append(self, data):
        self._size += 1
        p = node(data, None)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p

    def insert(self, index, data):
        p = node(data)

        if (index < 0 or index > self._size):
            pass
        elif (index == 0):
            p.next = self.head
            self.head = p
            self._size += 1
        else:
            temp = self.head
            for i in range(0, index - 1):
                if (temp != None):
                    temp = temp.next
            if (temp != None):
                p.next = temp.next
                temp.next = p
                self._size += 1 
            else:
                temp = self.head
                while(temp.next != None):
                    temp = temp.next
                temp.next = p
                self._size += 1

    def size(self):
        return self._size

    def printList(self):
        if self._size == 0:
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

if __name__ == '__main__':
    inp = input("Enter Input : ").split(',')
    l = LinkList()
    for i in inp:
        if ':' not in i:
            if i != "":
                data = i.split(' ')
                for i in data:
                    l.append(i)
                intr = l.head
            l.printList()
            # print("size :", l.size())

        else:
            ins = i.split(':')
            l.insert(int(ins[0].lstrip()), ins[1])
            if (int(ins[0]) < 0 or int(ins[0]) > l.size()):
                print("Data cannot be added")
            else:
                print("index =", ins[0].lstrip() ,"and data =", ins[1])
            l.printList()
            # print("size :", l.size())
