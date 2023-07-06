
# Write a Python program to square the elements of a list using map() function.



# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]

def square_num(n):
  return n * n
nums = list(map(int,input("enter a numbers:").split()))
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))