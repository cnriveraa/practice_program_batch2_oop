#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 < num2:
    print("The smaller number is: ", num1)
else:
    print("The smaller number is: ", num2)