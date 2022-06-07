class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        
        for i in range(len(tokens)):
            if tokens[i] == "+":
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(a + b)
            elif tokens[i] == "*":
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(a * b)
            elif tokens[i] == "-":
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(b - a)
            elif tokens[i] == "/":
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(int(b / a))
            else:
                num_stack.append(int(tokens[i]))
        return num_stack[0]
                    
                    
            