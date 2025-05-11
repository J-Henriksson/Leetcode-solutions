class HappyNumber(object):
    def is_happy(self, n: int) -> bool:
        used_numbers = []
        while True:
            n = self.get_square_sum(n)
            if n in used_numbers:
                return False
            used_numbers.append(n)
            if n == 1:
                return True
        
    def get_square_sum(self, n: int) -> int:
        digit = 0
        while n != 0:
            digit += (n % 10)**2
            n //= 10
        return digit
    

if __name__ == "__main__":
    happy_number = HappyNumber()
    print(happy_number.get_square_sum(64))
    print(happy_number.is_happy(19))