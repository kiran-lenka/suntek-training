class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = True
        for i in s:
            length = len(stack)
            if i =='{' or i =='(' or i =='[':
                stack.append(i)
            elif i == '}':
                if length!= 0 and stack[-1]=='{':
                    stack.pop()
                else:
                    valid = False
                    break
            elif i == ']':
                if length!= 0 and stack[-1]=='[':
                    stack.pop()
                else:
                    valid = False
                    break
            elif i == ')':
                if length!= 0 and stack[-1]=='(':
                    stack.pop()
                else:
                    valid = False
                    break
            else:
                break
        if len(stack) != 0:
            valid = False
        return valid
