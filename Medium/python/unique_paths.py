from math import factorial

class UniquePaths():

    def manual_factorial(self, m):
        if m == 0:
            return 0
        sum = 1
        for int in range(1, m + 1):
            sum *= int
        return sum 
    
    def binomial_coefficient(self, m, n):
        #m choose n
        return int(self.manual_factorial(m) / (self.manual_factorial(m - n) * self.manual_factorial(n)))

    def unique_paths(self, m, n):
        return int(factorial(n + m - 2) / (factorial(n - 1) * factorial(m - 1)))

if __name__ == "__main__":
    unique_paths = UniquePaths()

    print(unique_paths.unique_paths(3, 7))