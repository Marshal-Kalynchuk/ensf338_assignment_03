import threading
import time
import random

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def enqueue(self, item):
        with self.not_full:
            while self.count == self.capacity:
                self.not_full.wait(1)
            if self.count < self.capacity:
                self.buffer[self.tail] = item
                self.tail = (self.tail + 1) % self.capacity
                self.count += 1
                self.not_empty.notify()

    def dequeue(self):
        with self.not_empty:
            while self.count == 0:
                self.not_empty.wait(1)
            if self.count > 0:
                item = self.buffer[self.head]
                self.head = (self.head + 1) % self.capacity
                self.count -= 1
                self.not_full.notify()
                return item

def producer(queue):
    while True:
        item = random.randint(1, 10)
        time.sleep(item)
        queue.enqueue(item)

def consumer(queue):
    while True:
        item = random.randint(1, 10)
        time.sleep(item)
        value = queue.dequeue()
        if value is not None:
            print(value)

if __name__ == '__main__':
    q = Queue(10)
    t1 = threading.Thread(target=producer, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()