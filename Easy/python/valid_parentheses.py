class ValidParentheses():
    PARENTHESES = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
        
    def is_valid(self, s: str) -> bool:   
        stack = []
        for l in s:
            if l in self.PARENTHESES:
                stack.append(l)
            else:
                if len(stack) == 0:
                    return False
                if l != self.PARENTHESES.get(stack[len(stack) - 1]):
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True