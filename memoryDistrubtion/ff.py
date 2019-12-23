statue=[[0,0,100,1]]# 空间pid->所有空闲都是0 起始地址 大小 是否空 1空0非  
uid_map={}#uid与大小
pid_map={'free':0}#pid与uid映射
id_con=1#分配空间id计数器

def show():
    bar='*'*50
    for i in range(len(statue)):
        print(bar+str(statue[i][1]))
        for line in range(int(statue[i][2]/10)):
            print('*'+' '*48+'*')
        print(' '*15+'进程:'+list(pid_map.keys())[list(pid_map.values()).index(statue[i][0])]+' 大小:'+str(statue[i][2]))
        for line in range(int(statue[i][2]/10)):
            print('*'+' '*48+'*')
    print(bar)


def load(uid):
    global id_con
    flag=0
    pro=uid_map[uid]
    for one in statue:
        if one[3]==1:#判断是空闲区
            if one[2]>=pro:#判断有足够空间
                tem=[id_con,one[1],pro,0]#给新空间建表
                one[1]+=pro
                one[2]-=pro
                statue.insert(statue.index(one),tem)#更新空闲表
                if one[2]==0:#若空闲区正好大小等于程序 删除
                    del one
                pid_map[(uid)]=id_con#更新pid映射
                id_con+=1
                print("分配成功")
                break
            else:
                flag=1
        else:
            flag=2
    if(flag==1):
        #print("分配失败-空间不足")
        pass
    else:
        #print("分配失败-空闲区不足")
        pass


def release(pro_id):
    #删除表 检查且合并空闲区
    for i in range(len(statue)):
        if statue[i][0]==pro_id:
            tem_sta=statue[i][1]
            tem_size=statue[i][2]
            
            
            if i==0:#最前面的分区
                if statue[i+1][3]==1:#合并
                    statue[i+1][1]=tem_sta
                    statue[i+1][2]+=tem_size
                    del statue[i]
                else:
                    statue[i][0]=0
                    statue[i][3]=1
            elif i==len(statue)-1:#最后面分区
                if statue[i-1][3]==1:
                    statue[i-1][2]+=tem_size
                    del statue[i]
                else:
                    statue[i][0]=0
                    statue[i][3]=1
            else:#中间分区
                if statue[i-1][3]==1 and statue[i+1][3]==1:#上下都是空
                    statue[i-1][2]+=(tem_size+statue[i+1][2])
                    del statue[i+1],statue[i]
                elif statue[i-1][3]==1 and statue[i+1][3]==0:
                    statue[i-1][2]+=tem_size
                    del statue[i]
                elif statue[i-1][3]==0 and statue[i+1][3]==1:
                    statue[i+1][1]=tem_sta
                    statue[i+1][2]+=tem_size
                    del statue[i]
                else:
                    statue[i][0]=0
                    statue[i][3]=1
            break
            
        



def play():
    list = [int(n) for n in input("输入待分配进程空间大小\n").split()]
    for i in range(len(list)):
        dkey=chr(ord('a')+i)
        uid_map[(dkey)]=list[i]
    print(uid_map)
    while(1):
        try:
            op,item=input("输入操作数与uid 操作数：load release 其他输入即退出\n ").split()
            if(op=='load'):
                #TODO
                load(item)
                show()
            elif(op=='release'):
                #TODO
                release(pid_map[item])
                show()
                
        except ValueError as e:
            print("exit")
            exit(0)



if __name__=="__main__":
    play()
