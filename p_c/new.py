import threading, time, queue ,random
cache = queue.Queue(10)#缓存队列
flag=1#缓存控制只允许一个进程进入

def Produce():
    global flag
    count = 0   #conut表示生产的item总个数
    q=queue.Queue(10)
    while 1:
        count += 1#生产
        print('生产第%s个item中。。。'%count)
        q.put(count)
        time.sleep(3)
        if(flag==1 and (not cache.full())):
                cache.put(q.get())   # 缓冲区添加item
                print('投入缓存第%s个item'%count)
                


def Consumer():
    global flag
    while 1:
        if(not cache.empty()):
                flag=0
                data = cache.get()  # 取缓冲的物品
                print('消费中。。。')
                time.sleep(2)   
                print('消费了第%s个item'%data)
                flag=1

if __name__ == '__main__':
    p1 = threading.Thread(target=Produce)
    c1 = threading.Thread(target=Consumer)

    p1.start()
    c1.start()
