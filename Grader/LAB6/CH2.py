
def length(txt):     
    #Code Hereh
    if txt == '':
        return 0
    else:
        m = 1 + length(txt[1:])
        if m % 2 != 0:
            print( txt[0],'*', sep = '', end = '')
            return m
        elif m % 2 == 0:
            print( txt[0],'~', sep = '', end = '')
            return m
        else:
            txt = txt[::-1]
            print(txt[0], sep = '', end = '')
            return m

if __name__ == '__main__':
    inp = input("Enter Input : ")
    m = length(inp[::-1])
    print('\n',m,sep="")