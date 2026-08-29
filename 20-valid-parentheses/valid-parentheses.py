class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []   
        pairs = {
                 ']':'[',
                 ')':'(',
                 '}':'{'
               }

        for bracket in s:
            if bracket in '([{':
                stack.append(bracket)
            else:
                if not stack:
                    return False
                elif stack[-1] == pairs[bracket]: 
                    stack.pop()
                else:
                    return False
        
        return stack == []



        