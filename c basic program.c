// 1. Hello, World

#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
//*********************************************

// 2.Sum of Two Numbers

#include <stdio.h>

int main() {
    int num1, num2, sum;

    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);

    sum = num1 + num2;

    printf("Sum: %d\n", sum);
    return 0;
}

//************************************************

//3.Check Even or Odd

#include <stdio.h>

int main() {
    int num;

    printf("Enter an integer: ");
    scanf("%d", &num);

    if (num % 2 == 0)
        printf("%d is even.\n", num);
    else
        printf("%d is odd.\n", num);

    return 0;
}

//************************************************

// 4.Find Largest of Three Numbers

#include <stdio.h>

int main() {
    int num1, num2, num3;

    printf("Enter three integers: ");
    scanf("%d %d %d", &num1, &num2, &num3);

    if (num1 >= num2 && num1 >= num3)
        printf("Largest number: %d\n", num1);
    else if (num2 >= num1 && num2 >= num3)
        printf("Largest number: %d\n", num2);
    else
        printf("Largest number: %d\n", num3);

    return 0;
}

//***********************************************

// 5.Factorial of a Number

#include <stdio.h>

int main() {
    int num, i;
    unsigned long long factorial = 1;

    printf("Enter an integer: ");
    scanf("%d", &num);

    if (num < 0)
        printf("Error! Factorial of a negative number doesn't exist.\n");
    else {
        for (i = 1; i <= num; ++i) {
            factorial *= i;
        }
        printf("Factorial of %d = %llu\n", num, factorial);
    }

    return 0;
}

//***********************************************************

// 6.Prime Number Check

#include <stdio.h>

int main() {
    int num, i, flag = 0;

    printf("Enter a positive integer: ");
    scanf("%d", &num);

    if (num == 0 || num == 1) {
        flag = 1;
    } else {
        for (i = 2; i <= num / 2; ++i) {
            if (num % i == 0) {
                flag = 1;
                break;
            }
        }
    }

    if (flag == 0)
        printf("%d is a prime number.\n", num);
    else
        printf("%d is not a prime number.\n", num);

    return 0;
}

//******************************************************

//7.Fibonacci Sequence

#include <stdio.h>

int main() {
    int n, t1 = 0, t2 = 1, nextTerm;

    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Sequence: ");

    for (int i = 1; i <= n; ++i) {
        printf("%d, ", t1);
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }

    return 0;
}

//******************************************************************

// 8.Reverse a Number

#include <stdio.h>

int main() {
    int num, reversed = 0, remainder;

    printf("Enter an integer: ");
    scanf("%d", &num);

    while (num != 0) {
        remainder = num % 10;
        reversed = reversed * 10 + remainder;
        num /= 10;
    }

    printf("Reversed number: %d\n", reversed);
    return 0;
}
//*****************************************************************
