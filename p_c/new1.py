import threading, time, queue ,random
cache = queue.Queue(10)#缓存队列
count = 0   #conut表示生产的item总个数
lock=threading.Lock()
def Produce(id):
    global flag
    q=queue.Queue(10)
    while 1:
        global count 
        count += 1#生产
        print('%d号生产者生产%s个item中。。。'%(id,count))
        q.put(count)
        time.sleep(0.1)
        if(not cache.full()):
                lock.acquire()
                pin=q.get()
                cache.put(pin)   # 缓冲区添加item
                print('%d生产者投入缓存第%s个item'%(id,pin))
                ppp=cache.qsize()
                print('#'*ppp+'-'*(10-ppp))
                lock.release()


def Consumer(id):
    while 1:
        if(not cache.empty()):
                lock.acquire()
                flag=0
                data = cache.get()  # 取缓冲的物品
                time.sleep(0.2)   
                print('%d号消费了第%s个item'%(id,data))
                flag=1
                ppp=cache.qsize()
                print('#'*ppp+'-'*(10-ppp))  
                lock.release()

if __name__ == '__main__':
    p1 = threading.Thread(target=Produce,args=(1,))
    p2 = threading.Thread(target=Produce,args=(2,))
    p3 = threading.Thread(target=Produce,args=(3,))
    c1 = threading.Thread(target=Consumer,args=(1,))
    c2 = threading.Thread(target=Consumer,args=(2,))

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

