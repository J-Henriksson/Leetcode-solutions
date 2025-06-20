import timeit

class DpFibonacci:
    
    def __init__(self, mem=[0,1]):
        self.mem = mem
    
    def dynamic_fibonacci(self, n):
        if n > len(self.mem):
            for i in range(len(self.mem), n + 1):
                self.mem.append(self.mem[i - 1] + self.mem[i - 2])
        return self.mem[n]
class WorseFibonacci():
        
    def recursive_fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.recursive_fibonacci(n - 1) + self.recursive_fibonacci(n - 2)
    

if __name__ == "__main__":
    fib = DpFibonacci()
    worse_fib = WorseFibonacci()
    time_worse = timeit.timeit('worse_fib.recursive_fibonacci(25)', globals=globals(), number=1000)
    time_dynamic = timeit.timeit('fib.dynamic_fibonacci(25)', globals=globals(), number=1000)
    difference = time_worse - time_dynamic
    print("Dynamic programming fibonacci is {} seconds faster".format(difference))