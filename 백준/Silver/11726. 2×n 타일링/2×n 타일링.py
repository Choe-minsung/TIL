def rect(n):
    
    r_array = [1,2]
    
    for i in range(2, n+1): 
        r_array.append(r_array[i-1] + r_array[i-2])
        
    return r_array[n-1] % 10007 

print(rect(int(input())))