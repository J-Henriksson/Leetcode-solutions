class DpFibonacci:
    
    def __init__(self, mem=[0,1]):
        self.mem = mem
    
    def dynamic_fibonacci(self, n):
        if n > len(self.mem):
            for i in range(len(self.mem), n + 1):
                self.mem.append(self.mem[i - 1] + self.mem[i - 2])
        return self.mem[n]


if __name__ == "__main__":
    fib = DpFibonacci()
    print(fib.dynamic_fibonacci(45))