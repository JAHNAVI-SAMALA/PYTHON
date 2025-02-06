n = int(input())
def countPrimes(n):#sieve of eratosthenes
    isPrime=[1]*n
    count = 0
    for i in range(2,int(n**0.5)+1):
        if(isPrime[i] == 1):
            for j in range(i*i,n,i):
                isPrime[j] = 0
    for i in range(2,len(isPrime)):
        if(isPrime[i]==1):
            count += 1
    return count
print(countPrimes(n))
