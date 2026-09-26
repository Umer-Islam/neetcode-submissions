class Solution:
    def isValid(self, s: str) -> bool:

        length = len(s)
        if length%2!=0 or length ==0:
            return False
        stack = [] 
        for i in range(length):
            if s[i]== "(" or s[i]== "{" or s[i]== "[":
                stack.append(s[i]) 
            else:
                if(len(stack)==0):
                    return False
                else:
                    if (stack[-1]== "(" and s[i] ==')') or ( stack[-1]== "[" and s[i] ==']') or (stack[-1]== "{" and s[i] =='}'):
                        stack.pop()
                    else:
                        return False

        return False if len(stack)!=0 else True
        