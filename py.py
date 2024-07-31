# 1.Prime Number Check
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

#***********************************************

#2.Simple Calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")
  
#3. Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

s = input("Enter a string: ")
if is_palindrome(s):
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")

#4.Count Vowels in a String
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))
