def validparentheses(s):
    stack=[]
    d = {'}' : '{', ']' :'[',')':'('}
    for char in s:
        if char in '{[(':
            stack.append(char)
        else:
            if len(stack)==0:
                return False
            if stack[-1] ==  d[char]:
                stack.pop()
    return len(stack)==0
s= input()
print(validparentheses(s))
