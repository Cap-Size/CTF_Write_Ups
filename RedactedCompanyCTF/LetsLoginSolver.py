#needs only 10 results from the genValid function
#.... Thus put 10 in the ()


#init the lists
outList = []
newOutList = []

#Weird int that must input MOD int == 0
#...Thus is has to be a multiple of the int
num = 26953030255659232628

#creates a list of vali inputs from the if statment from the code
def genValid(numOfResults):
    for i in range(numOfResults):
        out = ""
        test = num * i
        test = str(test)
        for c in test:
            out += c
        outList.append(out)


#converts the weird output to a string
def numToString(theList):
    for element in theList:
        temp = element
        temp2 = ''
        while(temp != ''):
            if( (temp[0] == "1")):
                temp2 += chr(int(temp[0:3]))
                temp = temp[3:]
            else:
                temp2 += chr(int(temp[0:2]))
                temp = temp[2:]
        newOutList.append(temp2)
