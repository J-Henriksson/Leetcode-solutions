class StringToIntAtoi():
    def my_atoi(self, s: str) -> int:
        result = 0
        negative = False
        num_start = False
        
        
        for c in range(len(s)):
            digit = ord(s[c]) - ord("0")
            if num_start == False:
                if (10 > digit and digit >= 0) or s[c] == "-" or s[c] == "+":
                    num_start = True
                    if 10 > digit and digit >= 0:
                        result = digit
                    elif s[c] == "-":
                        negative = True
                elif s[c] != " ":
                    break
            else:
                if 10 > digit and digit >= 0:
                    result = result * 10 + digit
                else:
                    break
                
                
        if negative == True:
            result *= -1
            if result < -2**31:
                result = -2**31 
        elif result > 2**31 - 1:
            result = 2**31 - 1 
        return result
    
if __name__ == "__main__":
    MyAtoi = StringToIntAtoi()
    print(MyAtoi.my_atoi("42"))
    print(MyAtoi.my_atoi(" -042"))
    print(MyAtoi.my_atoi("1337c0d3"))
    print(MyAtoi.my_atoi("0-1"))
    print(MyAtoi.my_atoi("21474836460"))