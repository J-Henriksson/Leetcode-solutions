class RemapDigit():
    def max_dif(self, num: int) -> int:
        numbers = []
        last_nine = -1
        while num != 0:
            if num % 10 == 9 and last_nine == -1:
                last_nine = len(numbers) - 1
            elif num % 10 != 9:
                last_nine = -1
            numbers.append(num % 10)
            num //= 10
        
        max = 0
        min = 0
        for i in range(len(numbers)):
            if numbers[i] == numbers[last_nine]:
                max += 9 * (10 ** i)
            else:
                max += numbers[i] * (10 ** i) 
            if numbers[i] != numbers[-1]:
                min += numbers[i] * (10 ** i)
        return max - min
    
if __name__ == "__main__":
    remap = RemapDigit()
    print(remap.max_dif(11891))
    print(remap.max_dif(90))