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
    inp = input("Enter code,hint : ").split(',')
    # inp[0] = 'gjstu`uftu' inp[1] = 'f'
    q = Queue()

    num = ord(inp[1]) - ord(inp[0][0])

    for i in inp[0]:
        i = chr(ord(i) + num)
        q.enQuene(i)
        print(q.items)