#SJF短作业优先

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
    
    minLen=1000
    minIndex=-1
    print("current process has arrived:")
    print("name   waiting time   serving time")
    for n in curlist:
        print(label[n],end='       ')
        print(curtime-intime[n],end='              ')
        print(sertime[n])
        if sertime[n]<=minLen:
            minLen=sertime[n]
            minIndex=n

    curtime+=sertime[minIndex]
    print("------>%s process is using...<---------"%label[minIndex])
    order.append(label[minIndex])
    sleep(sertime[minIndex]/10)
    del intime[minIndex],sertime[minIndex],label[minIndex]

print("----all processes has completed----")
print("process order is:")
print(order)
