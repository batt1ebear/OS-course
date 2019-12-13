#外存有10个块  内存有三个块  每个100(B)
#页表 每条状态为 页号0 物理块号1 状态位2 访问数3 修改位4 外存地址5
#规则：当页号为-1不在内存中即状态为0
#tip:页号直接就能看状态位（摸鱼了）
#假设每个块运行时间相同
import time as t
import random
form=[[-1,0,0,0,0,0],[-1,1,0,0,0,100],[-1,2,0,0,0,200],[-1,3,0,0,0,300],[-1,4,0,0,0,400],[-1,5,0,0,0,500],[-1,6,0,0,0,600],[-1,7,0,0,0,700],[-1,8,0,0,0,800],[-1,9,0,0,0,900]]
uid_map={}#给程序一个名字 与物理块号对应
temPageId=[]#页表
PageID=0#内存页id计数器
missCount=0

for i in range(len(form)):
        dkey=chr(ord('a')+i)
        uid_map[(dkey)]=form[i]

def show():
    #TODO:传入调度方向 外存与内存状态图
    bar='*'*50
    print(bar)
    for i in range(3):
        for line in range(5):
            print('*'+' '*48+'*')
        try:
            print(' '*5+"页号："+str(form[temPageId[i]][0])+" 物理块："+str(form[temPageId[i]][1])\
            +" 状态位："+str(form[temPageId[i]][2])+" 访问数："+str(form[temPageId[i]][3])+"\n          修改位："+str(form[temPageId[i]][4])+" 外存地址："+str(form[temPageId[i]][5]))
        except IndexError:
            print("          空")
            print('*'+' '*48+'*')
        except TypeError:
            print("fuck")
        for line in range(5):
            print('*'+' '*48+'*')
        print(bar)
    t.sleep(1)

# 是否在-不在-是否满-满-释放-插入
#                 -不满-插入
#       -在-END
def run(order):
    global PageID
    global temPageId
    ######记得简化一下 页表
    for num in range(len(form)):
        if form[num][0]!=-1:
            temPageId.append(form[num][1])
    ########简化
    for i in range(len(order)):
        if order[i] in temPageId:
            form[4]=1
            print("%d未缺页"%order[i])
            show()

        else:#不在页内
            if(len(temPageId)<3):#有空间
                temPageId.append(order[i])
                form[order[i]][0]=PageID
                PageID+=1
                form[order[i]][2]=1
                print("%d缺页-直接调入"%order[i])
                show()
            else:#没空间 调出算法 这里就调出随机一个了 其实应该写一个FIFO
                inde=temPageId[2]
                form[inde][0]=-1
                form[inde][2]=0
                del temPageId[2]
                PageID-=1

                temPageId.append(order[i])
                form[order[i]][0]=PageID
                PageID+=1
                form[order[i]][2]=1
                print("%d缺页-调出%d后调入"%(order[i],form[inde][1]))
                show()





def main():
    order = [int(n) for n in input("输入进程执行顺序\n").split()]
    run(order)
    print("缺页率为%f"%(missCount/len(order)))

main()