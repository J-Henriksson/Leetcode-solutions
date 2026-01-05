class SoupServings():
    
    def soup(self, n: int) -> float:
        if n >= 4300:
            return 1
        mem = {}
        return 0.25 * (self.helper(n-100,n, mem) + self.helper(n-75,n-25, mem) + self.helper(n-50,n-50, mem) + self.helper(n-25,n-75, mem))
    
    def helper(self, a: int, b: int, mem) -> float:
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0 and b >= 0:
            return 1
        if b <= 0:
            return 0            
        else:
            if (a,b) not in mem:
                mem[(a,b)] = 0.25 * (self.helper(a-100,b, mem) + self.helper(a-75,b-25, mem) + self.helper(a-50,b-50, mem) + self.helper(a-25,b-75, mem))
            return mem[(a,b)]
        
        
if __name__ == "__main__":
    servings = SoupServings()
    print(servings.soup(50))
    print(servings.soup(100))
    