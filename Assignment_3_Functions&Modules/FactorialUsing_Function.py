
# Using loop
'''
def factorial(num):
    fact = 1
    while num >= 1:
        fact *= num
        num -= 1
    return fact

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")
'''

# Using recursion

def factorial(number):
    """
    Calculates factorial using recursion
    n! = n * (n-1) * (n-2) * .... * 1
    n! = n * (n-1)!
    """
    if number == 0 or number == 1:
        return 1
    else:
        result = number * factorial(number-1)
        return result

print(f"Factorial of 5 is: {factorial(5)}")
    

