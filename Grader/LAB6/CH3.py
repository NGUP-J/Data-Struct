def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(abs(b), abs(a % b))

if __name__ == '__main__':
    a, b = input('Enter Input : ').split()
    if int(a) == 0 and int(b) == 0:
        print('Error! must be not all zero.')
    else:
        m = gcd(int(a if a > b else b), int(b if b < a else a))
        print(f'The gcd of {a if a > b else b} and {b if b < a else a} is : {m}')