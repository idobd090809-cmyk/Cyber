import threading
count=0
lock=threading.Lock()
def Increase():
    global count
    for i in range(100000):
        lock.acquire()
        count+=1
        lock.release()
def Decrease():
    global count
    for i in range(100000):
        lock.acquire()
        count-=1
        lock.release()


t1=threading.Thread(target=Increase)
t2=threading.Thread(target=Decrease)
t1.start()
t2.start()
t1.join()
t2.join()
print("counter value",count)


