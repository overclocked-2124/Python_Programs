# Write a function named odd_one(L) that accepts a list L as argument. Except for one element, all other elements in L are of the same data type. The function odd_one should return the data type of this odd element.

# For example, if L is equal to [1, 2, 3.4, 5, 10], then the function should return the string float. This is because the element 3.4 is the odd one here, all other elements are integers.

def odd_one(L):
    count_int=0
    count_float=0
    count_str=0
    count_bool=0
    for i in L:
        if(type(i)==int):
            count_int+=1
        if(type(i)==float):
            count_float+=1
        if(type(i)==str):
            count_str+=1
        if(type(i)==bool):
            count_bool+=1
    if(count_int==1):
        return("int")
    if(count_float==1):
        return("float")
    if(count_str==1):
        return("str")
    if(count_bool==1):
        return("bool")
        
print(odd_one(eval(input().strip())))

#Time Complexity: O(n)