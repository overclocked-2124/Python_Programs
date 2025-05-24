"""
Program to return a list of tuples according to Goldbach Conjecture.
"""

def primefind(y):
    prime=[]
    is_prime = [True] * (y+1)
    is_prime[0]=is_prime[1]=False
    
    for i in range(2,int(y**0.5)+1,1):
        if is_prime[i]:
            for j in range(i*i,y+1,i):
                is_prime[j]=False
    
    return(is_prime)

def Goldbach(x):
    goldbaches = []
    is_prime = primefind(x-1) 
    
    for i in range(2,x//2+1,1):
        if(is_prime[i]):       
            if(is_prime[x-i]):
                goldbaches.append((i,x-i))
    
    return (goldbaches)
    

n=int(input())
print(sorted(Goldbach(n)))

# Time complexity: O(n log log n)
# Procedure: