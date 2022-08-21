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
    inp1,inp2 = input("Enter Input : ").split('/')
    inp1 = list(inp1.split(','))
    inp2 = list(inp2.split(','))

    q1 = Queue()
    q2 = Queue()
    q3 = Queue()

    for i in inp1:
        if '1 ' in i:
            q1.enQuene(i[2:])
        elif '2 ' in i:
            q2.enQuene(i[2:])
        elif '3 ' in i:
            q3.enQuene(i[2:])

    qq1 = Queue()
    qq2 = Queue()
    qq3 = Queue()
    
    for i in inp2:
        if 'E' in i:
            if i[2:] in q1.items:
                qq1.enQuene(i[2:])
            elif i[2:] in q2.items:
                qq2.enQuene(i[2:])
            elif i[2:] in q3.items:
                qq3.enQuene(i[2:])
        elif 'D' in i:
            if qq1.isEmpty() and qq2.isEmpty() and qq3.isEmpty():
                print("Empty")
            elif qq1.isEmpty() and qq2.isEmpty():
                print(qq3.deQuene())
            elif qq1.isEmpty():
                print(qq2.deQuene())
            else:
                print(qq1.deQuene())

