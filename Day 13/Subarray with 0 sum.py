# Github: Gaurgirl6117
# DAY 13 of DAY 100
# Subarray with 0 sum - GeeksorGeeks
# https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        sum = 0
        s = set()
        for i in range(n):
            sum += arr[i]
            
            if sum == 0 or sum in s:
                return True
            s.add(sum)
                
           
        return False
                
        
            
            
