import time
import random 
import heapq
import matplotlib.plyplot as plt

class IneffPriorityQueue:
    def __init__ (self):
        self.queue = []
        
    def enqueue(self, value):
        self.queue.append(value)
        
    def dequeue(self):
        min_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i] < self.queue[min_index]:
                min_index = i
        return self.queue.pop(min_index)


class EffPriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        heapq.heappush(self.queue, value)
    
    def dequeue(self):
        return heapq.heappop(self.queue)



def search_experiment():

    inefficient_times = []
    efficient_times = []
    
    
    for i in range(100):
        inefficient_queue = IneffPriorityqueue()
        start_time = time.time()
        for j in range(1000):
            inefficient_queue.enqueue(random.randint(0,999))
        for k in range(1000):
            inefficient_queue.dequeue()
        end_time = time.time()
        inefficient_times.append(end_time - start_time)
            
            
        efficient_queue = EffPriorityQueue()
        start_time = time.time()
        for n in range(1000):
            efficient_queue.enqueue(random.randint(0,999))
        for m in range(1000):
            efficient_queue.dequeue()
        end_time = time.time()
        efficient_times.append(end_time - start_time)


pit.hist(inefficient_times, bins=20, alpha=0.5, label='Inefficient')
pit.hist(efficient_times, bins=20, alpha=0.5, label='Efficient' )
plt.legend()
plt.label("Time")
plt.ylabel ("Measurements")
plt.show()

if __name__ == "__main__":
