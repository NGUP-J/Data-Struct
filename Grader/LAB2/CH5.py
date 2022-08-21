class funString():

    def __init__(self,string = ""):
        self.string = string
        self.aList = list(string)
        ### Enter Your Code Here ###

    def __str__(self):
        pass
        ### Enter Your Code Here ###

    def size(self) :
        return len(self.string)
        ### Enter Your Code Here ###

    def changeSize(self):
        return self.string.swapcase()
        ### Enter Your Code Here ###

    def reverse(self):
        l = self.aList[::-1]
        return ''.join(l)
        ### Enter Your Code Here ###

    def deleteSame(self):
        l = list(dict.fromkeys(self.aList))
        return ''.join(l)
       ### Enter Your Code Here ###



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())