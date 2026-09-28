class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        stack = [] 

    #    push the thing in stack if it is not a operator
        for char in tokens:
            if char == "+":
                stack.append(stack.pop()+stack.pop())
            elif char == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif char == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            elif char == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            else:
                print(char)
                stack.append(int(char))
    # if it is operator then get the last 2 elements, do the opeartion on them and them pop them and add their resultant
    # return the top of stack
        return stack[0]