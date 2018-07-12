howMany=input('選択肢はいくつありますか?')
number=int(howMany)
list=[]
for i in range(number):
    choice=input('選択肢を教えてください')
    choiceNumber=input('その選択肢をいくつにするか教えてください')
    for i in range(int(choiceNumber)):
        list.append(choice)
import random
random.shuffle(list)
while len(list)!=0:
    list[0]=input(list[0])
    if len(list[0])==0:
        list.pop(0)
    else:
        break

