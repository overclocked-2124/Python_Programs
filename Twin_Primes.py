def Twin_Primes(x,y):
    twin_primes=[]
    is_prime = [True] * (y+1)
    is_prime[0]=is_prime[1]=False
    
    for i in range(2,int(y**0.5)+1,1):
        if is_prime[i]:
            for j in range(i*i,y+1,i):
                is_prime[j]=False
    
    for i in range(x,y+1,1):
        if (is_prime[i] and is_prime[i+2]):
            twin =(i,i+2)
            twin_primes.append(twin)
    
    return (twin_primes)
        

n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))