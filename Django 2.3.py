input_string = input("Enter a list elements separated by space ")

print("\n")
userList = input_string.split()
print("user list is ", userList)

sum1 = 0
for num in userList:
    sum1 += int(num)
print("Sum = ", sum1)