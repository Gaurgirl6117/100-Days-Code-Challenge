# Github: Gaurgirl6117
# DAY 1 of DAY 100
# Large Factorial - InterviewBit
# https://www.interviewbit.com/problems/large-factorial/

class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        
        #A = ()
        
        #if A < 0:
        #    print ("The factorial does not exist")
        
        #elif A == 0:
        #   print ("1")
        
        #else: 
        fac = {0:1}
        for n in range (1, A+1):
            fac[n] = n*fac[n-1]
        return fac[A]
