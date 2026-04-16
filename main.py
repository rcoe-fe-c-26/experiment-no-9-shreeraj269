# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder:shreeraj
# Date:

print("--- Factorial Finder ---\n")

# Write your code here
num = int(input('Enter a number: '))
print("")
og_num = num
for a in range(1,num):
    num = num*a
print(f"Factorial of {og_num} is {num}")
