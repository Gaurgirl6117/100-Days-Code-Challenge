# Github: Gaurgirl6117
# DAY 3 of DAY 100
# Union of two arrays - GeeksorGeeks
# https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        union = set()
          
        
        for i in range (0,n):
            union.add(a[i])
        for j in range (0,m):
            union.add(b[j]) 
            
        N = len(union)
            
        return N
            
