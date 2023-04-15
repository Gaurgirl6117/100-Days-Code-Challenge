# Github: Gaurgirl6117
# DAY 2 of DAY 100
# Max Sum Contiguous Subarray - InterviewBit
# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        n = len(A)
        
        a = A[0]
        sum = 0
        res = max(A)
        
        for i in range (1,n):
            
            sum += A[i]
            
            if sum<0:
                sum = 0
            else:
                res = max(res, sum)
                
        return max(max(A),res)
        
