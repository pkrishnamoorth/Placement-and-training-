# 1. Simple Addition

a = 5
b = 3
sum = a + b
print("Sum:", sum)

#************************************************

# 2. Area of a Circle

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("Area of the circle:", area)

#****************************************************************

# 3. Check Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

#***************************************************************

# 4. Factorial of a Number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))

#****************************************************************

# 5. Fibonacci Sequence

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

num = int(input("Enter the number of terms: "))
print("Fibonacci sequence:", fibonacci(num))

#**************************************************************

# 6.  Prime Number Check

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num/2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#*************************************************************
