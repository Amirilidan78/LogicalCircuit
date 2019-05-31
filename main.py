class node :
    def __init__(self,data,num):
        self.data = data
        self.num = num
    def setNum(self,num):
        self.num = num
def swap (defList , row , i , j ) :
    temp = []
    temp.append(defList[row][i])
    temp.append(defList[row][j])
    defList[row][j] = temp[0]
    defList[row][i] = temp[1]
def checkTwoData(first,second):
    a1 = first
    a2 = iter(second)
    bool = 0
    for i in a1 :
        j = next(a2)
        if i != j and (i != '_' or j != '_') :
            bool = bool + 1
    if bool == 1 :
        return True
    else:
        return False
def checkBigOne(first,second):
    a1 = first
    a2 = iter(second)
    bool = 0
    for i in a1:
        j = next(a2)
        if i == j or i == '_' or j == '_':
            pass
        else :
            bool = bool + 1
    if bool == 0:
        return True
    else:
        return False
def newNum(first,second):
    a1 = first
    a2 = iter(second)
    r = ""
    for i in a1:
        j = next(a2)
        if j == i :
            r = r+i
        else :
            r= r+'_'
    return r

list = [
[ node(1,5) , node(1,5) , node(0,5) , node(0,5)],
[ node(0,5) , node(0,5), node(0,5) , node(0,5)],
[ node(1,5) , node(1,5), node(0,5) , node(0,5)],
[ node(1,5) , node(1,5) , node(0,5) , node(0,5)],
];


# 1th row
list[0][0].setNum('0000')
list[0][1].setNum('0001')
list[0][3].setNum('0010')
list[0][2].setNum('0011')
# 2th row
list[1][0].setNum('0100')
list[1][1].setNum('0101')
list[1][3].setNum('0110')
list[1][2].setNum('0111')
# 4th row
list[3][0].setNum('1000')
list[3][1].setNum('1001')
list[3][3].setNum('1010')
list[3][2].setNum('1011')
# 3th row
list[2][0].setNum('1100')
list[2][1].setNum('1101')
list[2][3].setNum('1110')
list[2][2].setNum('1111')

# print the list
for i in list :
    print()
    for j in i :
        # it has no error
        print(j.data,end=',')
print()
print('****************')

m1 = []
for i in list :
    for j in i :
        if j.data == 1 :
            m1.append(j.num)

matris = m1

def myFunction(first,second) :
    N = len(matris)

    if int(first) >= int(N - 1):
        return

    if checkTwoData(matris[first], matris[second]):
        temp = newNum(matris[first], matris[second])
        matris[first] = temp
        del matris[second]
        myFunction(0, 1)
        return

    if int(second) >= int(N - 1):
        myFunction(first + 1, first + 2)
        return

    myFunction(first, second + 1)

print('this is 1 midterms : '+f'{m1}')



myFunction(0,1)
print(matris)



input()