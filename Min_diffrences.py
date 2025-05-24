""" 
    Write a function find_Min_Difference(L, P) that accepts a list L of integers and P (positive integer) where the size of L is greater than P. 
    The task is to pick P different elements from the list L, where the difference between the maximum value and the minimum value in selected elements is minimum compared to other differences in possible subset of p elements. 
    The function returns this minimum difference value.
"""
def find_Min_Difference(l,n):
    l.sort(reverse=True)
    min_diff=l[0]-l[n-1]
    for i in range(0,len(l)-n+1,1):
        diff=l[i]-l[i+n-1]
        if min_diff>diff:
            min_diff=diff
    
    return(min_diff)
    
    
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))