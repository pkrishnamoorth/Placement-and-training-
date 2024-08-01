# 1. Fibonacci Sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

num = int(input("Enter the number of terms: "))
print(f"The first {num} terms of the Fibonacci sequence are: {fibonacci(num)}")

#**************************************************************************

#2.Temperature Converter
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

choice = input("Convert from (C)elsius or (F)ahrenheit? ")

if choice.upper() == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
elif choice.upper() == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")
else:
    print("Invalid choice")

#******************************************************************************

#3. Simple To-Do List
to_do_list = []

def show_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

def add_task():
    task = input("Enter a task: ")
    to_do_list.append(task)
    print(f"'{task}' has been added to your to-do list.")

def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    task_num = int(input("Enter the number of the task to remove: "))
    if 0 < task_num <= len(to_do_list):
        removed_task = to_do_list.pop(task_num - 1)
        print(f"'{removed_task}' has been removed from your to-do list.")
    else:
        print("Invalid task number")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")

#4.Prime Number Checker

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#***************************************************************

#5Prime Number Checker.
  def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
