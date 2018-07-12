job=input('仕事を入れてください')
name=input('名前を入れてください')
jobs=job.split()
names=name.split()
remainder='余り'
luck='足りない'
list=[]
def process(jobs):
    for i in range(len(jobs)):
        if len(jobs[0])==0:
            jobs.pop(0)
        else:
            list.append(jobs[0])
            jobs.pop(0)
            jobs.append(list[0])
            list.pop(0)
process(jobs)
process(names)
if len(jobs)<len(names):
    while len(jobs)!=len(names):
        jobs.append(remainder)
elif len(jobs)>len(names):
    while len(jobs)!=len(names):
        names.append(luck)
else:
    pass
import random
random.shuffle(jobs)
while len(jobs)!=0:
        print(names[0]+'…'+jobs[0])
        jobs.pop(0)
        names.pop(0)
