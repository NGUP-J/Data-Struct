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

if __name__ == '__main__':
    print("******** Parking Lot ********")

    m,s,o,n = input("Enter max of car,car in soi,operation : ").split()

    m,n = int(m),int(n)

    s = list(s.split(','))
    s1 = Stack()
    if '0' in s:
        pass
    else:
        for i in s:
            s1.push(int(i))
    if o in 'arrive:':
        if m == s1.size():
            print("car", n, "cannot arrive : Soi Full")
        elif n in s1.items:
            print("car", n, "already in soi")
        else:
            s1.push(n)
            print("car", n, "arrive! : Add Car", n)

        
    elif o in "depart":
        if s1.size() == 0:
            print("car", n, "cannot depart : Soi Empty")
        elif n in s1.items:
            s1.items.remove(n)
            print("car", n, "depart ! : Car",n , "was remove")
        else:
            print("car",n,"cannot depart : Dont Have Car", n)
    print(s1.items) 

### Enter Your Code Here ###