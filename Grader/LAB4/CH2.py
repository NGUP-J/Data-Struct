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

if __name__ == '__main__':
    inp = input("Enter Input : ").split(',')
    qEN = Queue()
    qES = Queue()
    for i in inp:
        if 'EN' in i:
            qEN.enQuene(i[3:])
        if 'ES' in i:
            ## แทรก
            qES.enQuene(i[3:])
        if 'D' in i:
            if qEN.isEmpty() and qES.isEmpty():
                print("Empty")
            elif qES.isEmpty():
                print(qEN.deQuene())
            else:
                print(qES.deQuene())
        