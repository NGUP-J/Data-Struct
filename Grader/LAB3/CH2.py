class Stack:

    def __init__ (self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def __str__(self):
        s = 'stack of' + str(self.size()) + 'items :'
        for ele in self.items:
            s += str(ele) + ''
        return s

    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def ManageStack(self, ls):
        if 'A' in ls:
            self.push(ls[2:])
            print("Add = " + ls[2:])
        elif 'P' in ls:
            if self.isEmpty():
                print(-1)
            else:
                print("Pop = " + self.pop())
        elif 'D' in ls and 'LD' not in ls and 'MD' not in ls:
            if self.isEmpty():
                print(-1)
            else:
                i = 0
                while i < (self.size()):
                    if int(self.items[i]) == int(ls[2:]):
                        print("Delete = " + self.items.pop(i))
                        i == 0
                    else:
                        i += 1
        elif "MD" in ls:
            if self.isEmpty():
                print(-1)
            else:
                i = (self.size()) - 1
                while i >= 0:
                    if int(self.items[i]) > int(ls[3:]):
                        intmd = self.items.pop(i)
                        print("Delete = " + intmd + " Because " + intmd + " is more than " +  ls[3:])
                        i = (self.size()) - 1
                    else:
                        i -= 1
        if "LD" in ls:
            if self.isEmpty():
                print(-1)
            else:
                i = (self.size()) - 1
                while i >= 0:
                    if int(self.items[i]) < int(ls[3:]):
                        intld = self.items.pop(i)
                        print("Delete = " + intld + " Because " + intld + " is less than " +  ls[3:])
                        i = (self.size()) - 1
                    else:
                        i -= 1
        


if __name__ == '__main__':
    ls = input("Enter Input : ").split(',')
    s = Stack()
    for i in range(len(ls)):
        s.ManageStack(ls[i])
    stg = str(s.items).replace('\'','')
    print("Value in Stack =",stg)