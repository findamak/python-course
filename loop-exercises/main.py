
# Print First 10 natural numbers using while loop
# i = 1
# while i < 11:
#     print(i)
#     i += 1

# ----------------------------------------------------------------------------
# Print the following pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# i = 1
# while i < 6:
#     for a in range(1,i):
#         print(a, end=" ")
#     i += 1
#     print("\n")

# ----------------------------------------------------------------------------
# Calculate the sum of all numbers from 1 to a given input number
# num = int(input("Enter a number: "))
# i = 1
# total = 0
# while i < num:
#     total = total + i
#     i += 1
# print(total + num)

# ----------------------------------------------------------------------------
# Write a program to print multiplication table of a given number
num = int(input("Enter number: "))
for i in range(1, 11, 1):
    new_num = num * i
    print(new_num)
