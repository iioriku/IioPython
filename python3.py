import numpy as np
import random
choices=input('選択肢を入れてください')
list=choices.split()
rate=input('確率を入れてください')
rate=rate.split()
rateList=[float(i) for i in rate]
while len(list)!=0:
    a=input(np.random.choice(list,p=rateList))
    if len(a)!=0:
        break
