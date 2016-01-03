import time
import random
import threading
import Queue

lock = threading.RLock()
queue = Queue.Queue(maxsize = 10)

class producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if lock.acquire():
                if not queue.full():
                    queue.put(1)
                    print 'prodecer : current queue size %d'%(queue.qsize())
                lock.release()
                time.sleep(random.randint(1,3))

class consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if lock.acquire():
                if not queue.empty():
                    queue.get()
                    print 'consumer : current queue size %d'%(queue.qsize())
                lock.release()
                time.sleep(random.randint(1,3))

if __name__ == '__main__':
    t1 = producer() 
    t2 = consumer() 
    t1.start()
    t2.start()
