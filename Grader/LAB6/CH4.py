def pantip(k, n, arr, path): # (k = money, n = len(arr), product price, product can buy)
    if n == len(arr):
        if k == sum(path): # if can buy fit money
            print(*path)
            return 1 # count pattern
        return 0 # count pattern
    return pantip(k, n+1, arr, path+[arr[n]]) + pantip(k, n+1, arr, path) # pattern conclusion

if __name__ == '__main__':
    inp = input('Enter Input (Money, Product) : ').split('/') # input data : money / product price
    arr = [int(i) for i in inp[1].split()] # convet str to int in list
    pattern = pantip(int(inp[0]), 0, arr, []) # return 
    print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern)) # print