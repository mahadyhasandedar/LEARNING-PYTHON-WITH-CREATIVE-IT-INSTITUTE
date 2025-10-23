
#1.Print numbers 1–10 Use a for loop to print numbers from 1 to 10.

for i in range(1, 11):
    print(i)

#2.sum of first N natural numbers Take input n, and find the sum using a for loop.

n = int(input("enter your number"))
sum = 0

for i in range(1, n + 1):
    sum = sum + i  

print(sum)

#3.Print even numbers from 1–50
# Use a for loop and an if statement.

for i in range (1,51):
    if i%2==0:
        print(i, "is even")
    else:
        print(i, "is odd")

# 4.Reverse counting
# Print numbers from 10 down to 1 using a while loop.

i = 10

while i >= 1:
    print(i)
    i = i - 1


# 5.Remove duplicates from list
# Use a loop (no sets) to build a list of unique elements.

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)



