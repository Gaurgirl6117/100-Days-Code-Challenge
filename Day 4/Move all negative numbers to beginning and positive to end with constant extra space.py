# Github: Gaurgirl6117
# DAY 4 of DAY 100
# Move all negative numbers to beginning and positive to end with constant extra space - GeeksorGeeks
# https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

list = []
n = int(input("Enter the number of elements in the array: "))

for i in range (0,n):
  ele = int(input())

  list.append(ele)

print(list)

list.sort()

print (list)
