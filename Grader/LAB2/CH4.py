import string

def hbd(age):
    i = 2
    while True:
        intr = (2 * (i**1)) # 20
        if intr + 1 == age: # 21
            return "saimai is just 21, in base " + str(i) + "!"
        if intr == age: # 20
            return "saimai is just 20, in base " + str(i) + "!"
        i += 1

year = input("Enter year : ")

print(hbd(int(year)))
