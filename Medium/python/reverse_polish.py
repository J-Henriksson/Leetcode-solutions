from typing import List
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}
class ReversePolish(object):

    #Method 2
    def eval_rpn(self, tokens: List[str]) -> int:
        i = 0
        while True:
            if tokens[i] in ops:
                tokens[i] = int(ops[tokens[i]](int(tokens[i - 2]), int(tokens[i - 1])))
                tokens.pop(i - 1)
                tokens.pop(i - 2)
                i -= 2
            i += 1
            if i > len(tokens) - 1:
                return int(tokens[i - 1])
    
    #Method 1
    def eval_rpn_stack(self, tokens: List[str]) -> int:
        stack = []
        for symbol in tokens:
            if symbol == "+":
                stack.append(stack.pop() + stack.pop())
            elif symbol == "-":
                stack.append(-1 * stack.pop() + stack.pop())
            elif symbol == "*":
                stack.append(stack.pop() * stack.pop())
            elif symbol == "/":
                stack.append(int((1 / stack.pop()) * stack.pop()))
            else:
                stack.append(int(symbol))
        return stack.pop()

if __name__ == "__main__":
    rpn_calc = ReversePolish()
    tokens_1 = ["2","1","+","3","*"]
    tokens_2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    tokens_3 = ["4","13","5","/","+"]
    print(rpn_calc.eval_rpn(tokens_1))
    print(rpn_calc.eval_rpn(tokens_2))
    print(rpn_calc.eval_rpn(tokens_3))

    print(rpn_calc.eval_rpn_stack(tokens_1))
    print(rpn_calc.eval_rpn_stack(tokens_2))
    print(rpn_calc.eval_rpn_stack(tokens_3))