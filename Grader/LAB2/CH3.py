def odd_even(type, data, mode):
    data = data.split()
    if type == 'S':
        data = ''.join(data)
    if mode == 'Odd':
        return data[::2]
    elif mode == 'Even':
        return data[1::2]
    
#     pass

print("*** Odd Even ***")
type, data, mode = input("Enter Input : ").split(',')

print(odd_even(type, data, mode))

# print(type)
# print(data)
# print(mode)