a = int(input("Enter a number:"))

def factorial(b):
    fact = 1
    for i in range(1,b + 1):
        fact *= i
    return fact



f = factorial(a)
print(f"The factorial of {a} is :{f}")


