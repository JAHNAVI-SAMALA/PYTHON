s="qwerqewerqqy"
d={}
for char in s:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1
print(d)
print(max(d.values()))
