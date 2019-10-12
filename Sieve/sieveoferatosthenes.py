def sieveOfEratosthenes(start,end) :
    prime = [True]*(end+1)
    res = []
    for i in range(2,end+1):
        if prime[i] :
            for j in range(i**2,end+1,i):
                prime[j] = False
    for i in range(start,end+1):
        if prime[i] :
            res.append(i)
    return res

start,end = map(int,input("Enter range to find prime numbers : ").split())
res = sieveOfEratosthenes(start,end)
print("List of prime numbers between "+str(start) + " and "+str(end)+" are : ")
print(res)
