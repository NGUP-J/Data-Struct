def Max(data):
    if len(data) <= 1:
        return data[0]
    else:
        m = Max(data[1:])
        return m if m > data[0] else data[0]

if __name__ == '__main__':
    inp = [int(a) for a in input('Enter Input : ').split()]
    print(f'Max : {Max(inp)}')
