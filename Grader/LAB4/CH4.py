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
    
    def isDep(self,dep):
        for i in self.items:
            if dep == i[0]:
                return True
        return False

    def insertQ(self, value):
        if self.isEmpty() or not self.isDep(value[0]):
            self.enQuene(value)
        else:
            for i in range(self.size()-1, -1, -1):
                if self.items[i][0] == value[0]:
                    self.items.insert(i+1, value)
                    return
            self.enQuene(value)

if __name__ == '__main__':
    inp1,inp2 = input("Enter Input : ").split('/')
    inp1 = inp1.split(',')

    emp = dict()
    for i in inp1:
        dep, idd = i.split()
        emp[idd] = dep

    inp2 = inp2.split(',')

    q = Queue()
    
    for i in inp2:
        if 'E' in i:
            q.insertQ((emp[i[2:]], i[2:]))
        elif 'D' in i:
            if not q.isEmpty():
                print(q.deQuene()[1])
            else:
                print("Empty")
