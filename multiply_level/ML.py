#多级反馈调度算法
import time as t
import matplotlib.pyplot as plt
import numpy as np
level0=[]
level1=[]
level2=[]

label=  ['a','b','c','d','e','f','g','h','i']
sertime=[2,4,5,7,8,5,10,15,20]#测试数据
intime=list(map(lambda x:x-2,sertime))#入时间
outtime=[0 for i in range(9)]#出时间

curtime=0

back=sertime[:]

level0=label
timeRound=2
print("-----第一队列 时间片为%d------"%timeRound)
for i in range(len(level0)):
    if sertime[i]>0:
        ##t.sleep(timeRound/10)
        sertime[i]-=timeRound
        if sertime[i]<=0:###如果该进程时间小于时间片
            curtime+=timeRound-abs(sertime[i])
            sertime[i]=0           
        else:
            curtime+=timeRound
        if sertime[i]==0:
            print("%s进程已经在 %d时间 完成"%(level0[i],curtime))
            outtime[i]=curtime
            
    else:
        pass


level1=level0
timeRound*=2
print("-----第二队列 时间片为%d------"%timeRound)
for i in range(len(level1)):
    if sertime[i]>0:
        #t.sleep(timeRound/10)
        sertime[i]-=timeRound
        if sertime[i]<=0:###如果该进程时间小于时间片
            curtime+=timeRound-abs(sertime[i])
            sertime[i]=0
        else:
            curtime+=timeRound
        if sertime[i]==0:
            print("%s进程已经在 %d时间 完成"%(level1[i],curtime))
            outtime[i]=curtime
            
    else:
        pass

level2=level1
timeRound*=2
while sum(sertime)>0:#直到空
    print("-----第三队列 时间片为%d------"%timeRound)
    for i in range(len(level2)):
        if sertime[i]>0:
            #t.sleep(timeRound/10)
            sertime[i]-=timeRound
            if sertime[i]<=0:###如果该进程时间小于时间片
                curtime+=timeRound-abs(sertime[i])
                sertime[i]=0
            else:
                curtime+=timeRound
            if sertime[i]==0:
                print("%s进程已经在 %d时间 完成"%(level2[i],curtime))
                outtime[i]=curtime
                
        else:
            pass

timero=[0 for i in range(9)]
wighro=[0 for i in range(9)]
for i in range(len(intime)):
    timero[i]=outtime[i]-intime[i]
    wighro[i]=timero[i]/back[i]

plt.rcParams['font.family'] = ['sans-serif']  
plt.rcParams['font.sans-serif'] = ['SimHei']

bar_width = 0.3 #柱形图宽度
plt.figure() #实例化一个画布
plt.bar(x=np.arange(len(label))-bar_width/2,height=timero,width=bar_width,color='r')
plt.bar(x=np.arange(len(label))+bar_width/2,height=wighro,width=bar_width,color='b') 

plt.ylabel('时间') #设置y轴名称
plt.title('周转时间与带权周转') #设置图片名称
plt.show()
