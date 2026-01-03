from typing import List
class PlusOne():
    
    def plus_one(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] += 1
        
        for i in range(len(digits) -1, -1, -1):
            if digits[i] < 10:
                break
            digits[i] %= 10
            if i == 0:
                digits.insert(0,1)
            else:
                digits[i - 1] += 1            
        
        return digits
            
    
if __name__ == "__main__":
    adder = PlusOne()
    digits = [1, 2, 9]
    digits_2 = [9, 9, 9]
    print(adder.plus_one(digits))
    print(adder.plus_one(digits_2))