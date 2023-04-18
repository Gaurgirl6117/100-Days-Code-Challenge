# Github: Gaurgirl6117
# DAY 5 of DAY 100
# Cyclically rotate an array by one - GeeksorGeeks
# https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1

def rotate( arr, n):
    
    for i in range (1,n):
        arr.insert(0, arr[-1])
        arr.pop()
        
        return arr
        
    
    
