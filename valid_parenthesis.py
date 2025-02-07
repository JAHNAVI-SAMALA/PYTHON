#valid parenthesis
S = input().strip()
stack = []
d = { ']' : '[','}':'{',')':'('}
for i in S:
   if i in d.values():
       stack.append(i)
   elif i in d:
       if stack and stack[-1] == d[i]:
           stack.pop()
       else:
           print("False")
           break
else:
    if not stack:
        print("True")
    else:
        print("False")
