'''
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
 
'''

num = int(input('Enter a number: '))

def factorial(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num*factorial(num-1)
fact = factorial(num)
print(f'Factorial of {num} is:' , fact)

'''
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
 
'''

num = int(input('Enter a number: '))
fact = 1 
if num == 0 or num == 1:
    print(f'Factorial of {num} is:', fact)
else:
    for i in range(1, num+1):
        fact *=i
    print(f'Factorial of {num} is:', fact)