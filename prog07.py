#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
even = 0
for i in range(10):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        even += 1
        print("The number of even numbers is: ", even)