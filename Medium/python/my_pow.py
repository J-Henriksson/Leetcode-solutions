class MyPow():
    #Runtime: Beats 100% Memory: Beats 32.28%
    def my_pow(self, x: float, n: int) -> float:
        return self.recursive_pow(x, n)

    def recursive_pow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return self.recursive_pow(1 / x, -n)
        elif n % 2 == 0:
            return self.recursive_pow(x * x, n / 2)
        return x * self.recursive_pow(x * x, (n - 1) / 2)


if __name__ == "__main__":
    my_pow = MyPow()
    print(my_pow.my_pow(2.0, 2))