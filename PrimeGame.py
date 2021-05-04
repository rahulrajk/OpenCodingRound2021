def sendPrimes(l,r,i):
    for k in range(l,r,i):
        if k==1:
            continue
        flag = 1
        for h in range(2,k//2+1):
            if k%h==0:
                flag = 0
                break
        if flag==1:
            return k
    else:
        return 0

def main():
    n = int(input())
    for i in range(n):
        l,r = map(int,input().split())
        primes = []
        # Finding the lowest prime
        ele = sendPrimes(l,r+1,1)
        if ele!=0:
            primes.append(ele)
        # Finding the largest prime
        ele = sendPrimes(r,l,-1)
        if ele!=0:
            primes.append(ele)
        if len(primes)!=0:
            m = min(primes)
            x = max(primes)
            print(x-m)
        else:
            print(-1)
main()
