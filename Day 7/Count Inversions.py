# Github: Gaurgirl6117
# DAY 7 of DAY 100
# Count Inversions - GeeksorGeeks
# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
    
  
#Function to count inversions in the array.
    
   
def inversionCount(self, arr, n):
        
        inv_count = 0 
        
        for i in range(n):
            for j in range(i+1, n):
                if (arr[i] > arr[j]):
                    inv_count += 1
                    
        
                    
        return inv_count    
                    
   

