number1=input('最初の数字を入れてください')
number2=input('最後の数字を入れてください')
number3=input('外す数字を入れてください')
erace=number3.split()
list=[i for i in range(int(number1),int(number2)+1)]
while len(erace)!=0:
    list.remove(int(erace[0]))
    erace.remove(erace[0])
import random
random.shuffle(list)
while len(list)!=0:
    listNumber=input(list[0])
    if len(listNumber)==0:
        list.pop(0)
    else:
        break
