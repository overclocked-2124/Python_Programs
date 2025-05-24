"""
Twin primes are pairs of prime numbers that differ by 2. For example (3, 5), (5, 7), and (11,13) are twin primes.

Write a function Twin_Primes(n, m) where n and m are positive integers and n < m , that returns all unique twin primes 
between m and n (both inclusive). The function returns a list of tuples and each tuple (a,b) represents one unique twin 
prime where n <= a < b <= m.
"""

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

# Time Complexity: O(n log log n) 