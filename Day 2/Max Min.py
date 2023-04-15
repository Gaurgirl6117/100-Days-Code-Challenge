# Github: Gaurgirl6117
# DAY 2 of DAY 100
# Max Min - InterviewBit
# https://www.interviewbit.com/problems/max-min-05542f2f-69aa-4253-9cc7-84eb7bf739c4/

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        
        max = A[0]
        min = A[0]
        for i in range(1, n):
            if A[i] > max:
                max = A[i]
            elif A[i] < min:
                min = A[i]
        
        sum = (max+min)
        return(sum)        
       
        
