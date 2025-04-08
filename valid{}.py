def validparentheses(s):
    stack=[]
    for char in s:
        if char=='{':
            stack.append(char)
        else:
            if len(stack)==0:
                return False
            if stack[-1] == '{' and char=='}':
                stack.pop()
    return len(stack)==0
s= input()
print(validparentheses(s))
