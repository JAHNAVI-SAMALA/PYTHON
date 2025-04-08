'''you are working in a company.
the company has m experienced employees and n freshers.
so the company is thinking to form teams of 4 such that each team has 1 experienced and 1 fresher .
so given m and n find the maximum team you can form'''

m,n = map(int,input().split())
print(min((m+n)//4,m,n))


#OR

m,n = map(int,input().split())
teams = 0
while m>0 and n>0 and m+n>= 4:
    if m>n:
        m=m-3
        n=n-1
    elif m<n:
        m=m-1
        n=n-3
    else:
        m=m-2
        n=n-2
    teams += 1
print(teams)

