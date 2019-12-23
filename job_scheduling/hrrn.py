#HRRN高响应比优先调度算法

intime=[0,5,10,10,20,25]#进程调入时间 事先排好序
sertime=[10,1,20,1,100,1]#进程所需cpu服务时间
label=['a','b','c','d','e','f']
curtime=0
order=[]

print('*'*45)
print("test data:")
print("process name:"+str(label[:]))
print("in time     :"+str(intime[:]))
print("serving time:"+str(sertime[:]))
print('*'*45)

from time import sleep

while sertime:
    print('*'*45)
    print("current time is %d"%curtime)
    curlist=[]
    for i in range(len(intime)):
        if intime[i]<=curtime:
            curlist.append(i)#当前已经到达的进程索引
    
    ratioMax=0
    maxIndex=0
    print("current process has arrived:")
    print("name   waiting time   serving time    ratio")
    for n in curlist:
        ratio=(curtime-intime[n]+0.01)/sertime[n]
        print(label[n],end='       ')
        print(curtime-intime[n],end='              ')
        print(sertime[n],end='               ')
        print(ratio)
        if ratio>=ratioMax:
            ratioMax=ratio
            maxIndex=n#在已到达进程获取最高响应比的索引 加0.01是防止分子为0


    curtime+=sertime[maxIndex]
    print("------>%s process is using...<---------"%label[maxIndex])
    order.append(label[maxIndex])
    sleep(sertime[maxIndex]/10)
    del intime[maxIndex],sertime[maxIndex],label[maxIndex]

print("----all processes has completed----")
print("process order is:")
print(order)
