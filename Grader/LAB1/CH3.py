

# input
print("*** Reading E-Book ***")
istr = input("Text , Highlight : ")
strlist = list(istr)
for x in range(len(strlist)):
    if strlist[x] == ",":
        Text = strlist[:x]
        Highlight = strlist[x+1:]
        break

# print(Text)
# print(Highlight)

# solution
nText = Text
i = 0
while i <= len(nText)-1:
        # print("i = ", i)
        if nText[i] == Highlight[0]:
            nText.insert(i, "[")
            nText.insert(i+2, "]")
            # print(nText)
            i += 2
            # print(i)
        if i == len(nText):
            break
        i += 1

# output
nstr = ''.join(map(str,nText))
print(nstr)