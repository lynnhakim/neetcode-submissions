class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        ( 1 + 4 ) 2 * - 3 -> 
        (1 4 + 2 * 3 -)
        1 not in ops-> turn to int 
        1 4 not in ops -> turn to int and add to stack
        + in ops -> stack.pop(1) + stack.pop(4)
        stack.append(5)
        stack.append(2)
        * in ops -> stack.pop(5) * stack.pop(2)
        stack.append(10)
        stacl.append(3)
        - in ops -> stack.pop(10) - stacl.pop(3)
        stack.append(3)
        return stack[-1]
        [a, b]
        a- b 
        """
        ops = {"+", "*", "-", "/"}
        stack = []
        for tok in tokens:
            if tok not in ops:
                stack.append(int(tok))
            else: 
                b, a = stack.pop(), stack.pop()
                if tok == "+":
                    stack.append(a + b) 
                if tok == "-":
                    stack.append(a - b) 
                if tok == "*":
                    stack.append(a * b) 
                if tok == "/":
                    stack.append(int(a/ b) ) 
        return stack[-1]
