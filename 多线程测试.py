import time
# from multiprocessing import Process
import threading

num = 0


def run():
    global num
    for i in range(4):
        print("i am running {}".format(i))
        time.sleep(2)
        num=num+1
        print(num)

def swim():
    global num
    for i in range(4):
        print("i am swimming {}".format(i))
        time.sleep(2)
        num = num + 1
        print(num)
if __name__ == '__main__':
    p1 = Process(target=run)
    p2 = Process(target=swim)


    p1 = threading.Thread(target=run)
    p2 = threading.Thread(target=swim)
    timeStart = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # swim()
    timeEnd = time.time()
    sumTime = timeEnd - timeStart
    print("time cost",sumTime)


    # p1.join()join 的作用是阻塞主进程，等join的进程结束后再继续
    # p2.join()
    print("it is main")
