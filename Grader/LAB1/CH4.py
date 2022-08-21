# input
print("*** Fun with Drawing ***")
x = int(input("Enter input : "))

# solution and output
width = int((x*4) - 3)
height = int((x*4) - 3) // 2

res = ['#' * width]

for i in range(height-1):
    curr = '#'
    if i % 2 == 0:
        for i in range(i//2):
            curr += '.#'
        curr = curr + '.' * (width - len(curr)*2) + curr
        res.append(curr)
    else:
        for i in range(i//2+1):
            curr += '.#'
        curr = curr + '#' * (width - len(curr)*2) + curr
        res.append(curr)

middle = '.'.join(['#'] * ((width//2) + 1))

print(*res, sep='\n')
print(middle)
print(*res[::-1], sep='\n')