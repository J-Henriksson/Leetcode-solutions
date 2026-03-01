class AddBinary():
    
    def add_binary(self, a: str, b: str) -> str:
        ans, rest, i = "", 0, 0
        
        while not (rest == 0 and i > max(len(a), len(b)) - 1):
            num1 = int(a[len(a) - 1 - i]) if i < len(a) else 0
            num2 = int(b[len(b) - 1 - i]) if i < len(b) else 0
            add = num1 + num2 + rest
            if add > 1:
                rest = 1
            else:
                rest = 0
            ans = str(add % 2) + ans
            i += 1
        return ans
            

if __name__ == "__main__":
    adder = AddBinary()
    
    print(adder.add_binary("001", "11"))
    