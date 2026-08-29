class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []   
        for bracket in s:
            if bracket in '([{':
                stack.append(bracket)
            else:
                if not stack:
                    return False
                elif (
                        (bracket == ')' and stack[-1] == '(') or 
                        (bracket == ']' and stack[-1] == '[') or
                        (bracket == '}' and stack[-1] == '{')
                     ): 
                        stack.pop()
                else:
                    return False
        
        return stack == []



        