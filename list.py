listx = []

def checkNumbers(min,max):
    tmp = ""
    flag = 1
    while True:
        tmp = input()
        flag = 1
        for i in range(len(tmp)):
            if tmp[i]>='0' and tmp[i]<='9':
                continue
            else:
                flag = 0
                print("Ошибка!! Введите число в диапазоне [",min,";",max,"]")
                break
        if flag == 1:
            res = int(tmp)
            if res>=min and res<=max and i == len(tmp)-1:
                break
            else:
                print("Ошибка!! Введите число в диапазоне [", min, ";", max, "]")
    return res
def kingMoves():
    print("Как может ходить король:")
    print("0 - вверх,")
    print("1 - вправо - вверх,")
    print("2 - вправо,")
    print("3 - вправо - вниз,")
    print("4 - вниз,")
    print("5 - влево - вниз")
    print("6 - влево,")
    print("7-  влево - вверх")

def printList():
    for x in listx:
        print(x[0], x[1])

def add(x, y):
    if x < listx[0][0]:
        listx.insert(0, (x, [y]))   # А это - в начало
        return 0

    for i in range(len(listx)):
        if x == listx[i][0]:
            if y in listx[i][1]:
                return 1  # y нашли, король здесь был
            else:
                listx[i][1].append(y)
                return 0  # Иначе дублирует еще и в конец :(

    listx.append((x, [y]))
    return 0

def createList(n):
    x = y = 0
    listx.append((x, [y]))
    ok = 0
    while n:
        print("Введите значение  ", end="")
        k = checkNumbers(0,7)
        if k == 0:
            y += 1
        elif k == 1:
            y += 1
            x += 1
        elif k == 2:
            x += 1
        elif k == 3:
            y -= 1
            x += 1
        elif k == 4:
            y -= 1
        elif k == 5:
            x -= 1
            y -= 1
        elif k == 6:
            x -= 1
        elif k == 7:
            x -= 1
            y += 1
        n -= 1
        ok = add(x, y)

        if ok == 1:
            print()
            print("Король здесь был")
            break
    return ok
#main

kingMoves()
print("Введите кол-во ходов короля: ", end="")
n = checkNumbers(1,100)
print("---------------------------------------------------------")
res = createList(n)
print("---------------------------------------------------------")
if res == 0:
    print("Король здесь не был")

print("Печать координат точек, через которые проходил король")
printList()
