stack = []
stack. append(10)
stack.append(20)
stack.pop()
isempty = len(stack)==0
if not isempty:
    top=stack[-1]
else:
    top=-1
print(stack) 
