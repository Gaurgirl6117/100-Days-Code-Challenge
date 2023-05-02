# Github: Gaurgirl6117
# DAY 11 of DAY 100
# Count pairs with given sum - GeeksorGeeks
# https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        c=0
        mp={}
        for i in range(n):
            target=k-arr[i]
            if target in mp:
                c+=mp[target]
            if arr[i] in mp:
                mp[arr[i]]+=1
            else:
                mp[arr[i]]=1
        return c
