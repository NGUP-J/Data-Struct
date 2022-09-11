class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def enQuene(self,i):
        self.items.append(i)

    def deQuene(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

if __name__ == '__main__':
    inp = input("Enter Input : ").split(',')
    q = Queue()
    for i in inp:
        if 'E' in i:
            q.enQuene(i[2:])
            print(q.size())
        if 'D' in i:
            if q.isEmpty():
                print(-1)
            else:
                print(q.items[0], q.items.index(q.items[0]))
                q.deQuene()
    if q.isEmpty():
        print("Empty")
    else:
        print(' '.join(q.items))
