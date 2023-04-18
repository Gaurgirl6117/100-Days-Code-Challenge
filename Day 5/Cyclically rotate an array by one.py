# Github: Gaurgirl6117
# DAY 5 of DAY 100
# Cyclically rotate an array by one - GeeksorGeeks
# https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1

def rotate( arr, n):
    x = arr[n-1]
    
    for i in range(0,n):
        a = arr[i]
        arr[i] = arr[n-1]
        arr[n-1] = a 
        
    return arr
        
    
    
