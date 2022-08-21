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


def postFixeval(st):

    s = Stack()
    for a in st:
        if a.lstrip('-').isdigit():
            s.push(a)
            continue

        op1, op2 = s.items.pop(), s.items.pop()

        if a == '+':
            s.push(float(op2) + float(op1))
        elif a == '-':
            s.push(float(op2) - float(op1))
        elif a == '*':
            s.push(float(op2) * float(op1))
        elif a == '/':
            s.push(float(op2) / float(op1))
    ### Enter Your Code Here ###

    return s.pop()

if __name__ == '__main__' :
    print(" ***Postfix expression calcuation***")

    token = list(input("Enter Postfix expression : ").split())
    Ans = postFixeval(token)
    print("Answer : ",'{:.2f}'.format(Ans))
