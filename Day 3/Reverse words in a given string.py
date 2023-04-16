# Github: Gaurgirl6117
# DAY 3 of DAY 100
# Reverse words in a given string - GeeksorGeeks
# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        
        RS = S.split('.')
        RS.reverse()
        RS = '.'.join(RS)
        
        return RS
