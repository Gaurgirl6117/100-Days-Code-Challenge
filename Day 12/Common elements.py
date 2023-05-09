# Github: Gaurgirl6117
# DAY 12 of DAY 100
# Common elements - GeeksorGeeks
# https://practice.geeksforgeeks.org/problems/common-elements1132/1

#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        a = set(A)
        b = set(B)
        c = set(C)
        
        inter_ab = a.intersection(b)
        inter_abc = inter_ab.intersection(c)
        
        l = list(inter_abc)
        l.sort()
        return l
        
        
