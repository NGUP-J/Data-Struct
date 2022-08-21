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

    def wood(self,ls):
        self.push(ls[2:])

    def lookback(self):
        count = 0
        x = 0
        for i in reversed(self.items):
            if int(i) > x:
                count += 1
                x = int(i)
            elif int(i) < x:
                continue
        print(count)
    
    def manage(self,ls):
        if 'A' in ls:
            self.wood(ls)
        elif 'B' in ls:
            self.lookback()

if __name__ == '__main__' :
    S= Stack()
    inp = input('Enter Input : ').split(',')
    for i in range(len(inp)):
        S.manage(inp[i])
