
#6. Conditional Statement Exercises (if, elif, else)

#6.1 Check if a given number is positive, negative, or zero.

num= int(input("enter your number :"))

if num > 0 :
    print("positive")

elif num <=-1 :
    print("negative")
else:
    print("zero")


#6.2 Take a number as input and print whether it is even or odd.

chikichiki= int(input("enter your chikichiki: "))

if chikichiki >100:
    print("odd")
elif chikichiki <-1 or 1 :
    print("yoyo")
else:
    print("even")


#6.3 Ask for a user's age and print if they are a child, teenager, or adult.

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

#6.4 Compare two numbers and print which one is greater, or if they are equal.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is greater.")
elif num2 > num1:
    print("Second number is greater.")
else:
    print("Both numbers are equal.")


#6.5 Take a score (0–100) and assign a grade (A, B, C, D, F).

score = int(input("Enter your score (0–100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")





