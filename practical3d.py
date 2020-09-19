## Practical 3(D)
'''
Program to calculate factorial and
to compute the factors of given number
(i) Using recursion
(ii) Using iteration

'''

def factorial_iter(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact

def factors_iter(num):
    fact = 1
    for i in range(1,num+1):
        if (num%i == 0):
            print(i,end =' ')

def factorial_recur(num):
    if (num == 0) or (num == 1):
        return 1
    temp = factorial_recur(num-1)
    return num*temp

def factor_recur(num,i):
    temp = 1
    if (i <= num):
        if (num % i == 0):
            print(i,end = ' ')
        factor_recur(num,i+1)


number = int(input("Enter a number: "))
print("\nFactorial using iteration: ",factorial_iter(number))
print("Factors of",number,"using iteration:")
factors_iter(number)
print("\n\nFactorial using recursion: ",factorial_recur(number))
print("Factors of",number,"using recursion:")
factor_recur(number,1)


