def factorial(num):
    fact = 1
    while num >= 1:
        fact *= num
        num -= 1
    return fact

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")
