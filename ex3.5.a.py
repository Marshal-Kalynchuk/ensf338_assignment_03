import time
import random 
import matplotlib.plyplot as plt

# inefficient implementation (linear search):
def linear_search(arr, x):
    for i in range(len (arr)):
        if arr [i] == x:
            return i
        return -1

# efficient implementation (binary starch):
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# experiment:


def search_experiment ():
    arr = [random.randint (0, 999) for i in range (1000)]
    
    linear_times = []
    binary_times = []
    
    for i in range (100):
        x = random.choice (arr)
        start_time = time.time()
        linear_search(arr, x)
        linear_times.append (time.time() - start_time)
        
        start_time = time.time()
        binary_search(arr, x)
        binary_times.append(time.time() - start time)
        
        
        plt.hist(linear_times, bins=20, alpha=0.5, label='Linear')
        plt.hist(binary_times, bins=20, alpha=0.5, label='Binary')
        pit.legend ()
        plt.xlabel("Time")
        pt.ylabel ("Measurements")
        plt.show()


if __name__ == "__main__":
