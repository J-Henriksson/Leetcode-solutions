class Sqrt(object):
    def my_sqrt(self, x: int) -> int:
        bottom = 0 
        if x < 1:
            top = 1
        else:
            top = x
        while top >= bottom:
            mid = (top + bottom) / 2
            
            if mid * mid > x:
                top = mid
            elif mid * mid < x:
                bottom = mid
            else:
                return mid
            
    def my_sqrt_integer(self, x: int) -> int:
        bottom = 0 
        if x < 1:
            top = 1
        else:
            top = x
        result = 1
        while top >= bottom:
            mid = (top + bottom) // 2
            
            if mid * mid > x:
                top = mid - 1
            else:
                bottom = mid + 1
                result = mid
        return result
        
if __name__ == "__main__":
    sqrt = Sqrt()
    print(sqrt.my_sqrt(9))
    print(sqrt.my_sqrt_integer(9))
