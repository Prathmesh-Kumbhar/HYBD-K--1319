
## Print the table using Function and get the input from user

number=int(input("Enter a Number : "))

def table(num):
    for i in range(1,11):
        print(f"{num}*{i} = ",num*i)
table(number)
'''
5*1 =  5
5*2 =  10
5*3 =  15
5*4 =  20
5*5 =  25
5*6 =  30
5*7 =  35
5*8 =  40
5*9 =  45
5*10 =  50

'''

## Check the number is Palindrome or not using function

num=int(input("Enter a Number : "))
def palindrome(num):
    str_num=str(num)
    rev_str=str_num[::-1]
    if rev_str==str_num:
        print("Number is Palindrome")
    else:
        print("Number is Not Palindrome")
palindrome(num)

'''
Enter a Number : 122
Number is Not Palindrome

Enter a Number : 121
Number is Palindrome
'''

## Print the reverse list using function

list=[10,20,30,40,50,60]

def rev_list(list):
        print(list[::-1])
rev_list(list)

'''
[60, 50, 40, 30, 20, 10]
'''
## Print the Right angle star pattern using function

num=int(input("Enter number of Rows : "))

def right_angle(num):
    for i in range(1,num+1):
        for j in range(i):
            print("*",end=" ")
        print()
right_angle(num)

'''
Enter number of Rows : 5
* 
* * 
* * * 
* * * * 
* * * * * 
'''

## Print reverse of right angle triangle

num=int(input("Enter number of Rows : "))

def right_angle(num):
    for i in range(num,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()
right_angle(num)

'''
Enter number of Rows : 5
* * * * * 
* * * * 
* * * 
* * 
*
'''
## Print the Square of star pattern

num=int(input("Enter number of Rows : "))

def right_angle(num):
    for i in range(1,num+1):
        for j in range(1,num+1):
            print("*",end=" ")
        print()
right_angle(num)

'''
Enter number of Rows : 5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

'''

## Check the number is Even or Odd using Function

num=int(input("Enter a Number : "))

def check(num):
    if num%2==0:
        print("Number is Even.")
    else:
        print("Number is Odd.")
check(num)

'''
Enter a Number : 12
Number is Even.

Enter a Number : 15
Number is Odd.

'''
## Check the given number is Prime or not

num = int(input("Enter a Number : "))

def prime(num):
    count = 0
    
    for i in range(2, num):
        if num % i == 0:
            count += 1

    if count == 0:
        print("Number is Prime.")
    else:
        print("Number is Not Prime.")

prime(num)

'''
Enter a Number : 15
Number is Not Prime.

Enter a Number : 7
Number is Prime.

'''
## Q) you have a given a number . if the number is divisible by 3 display "FIZZ" divisible by 5 Disply "BUZZ " and divisible by 3 and 5 display "FIZZBUZZ"

num=int(input("Enter a Number : "))

def divisible(num):
    if num%3==0 and num%5==0:
        print("FIZZBUZZ")
    elif num%3==0:
        print("FIZZ")
    elif num%5==0:
        print("BUZZ ")
    else:
        print("Number is Not divisible by 3 and 5")

divisible(num)

'''
Enter a Number : 7
Number is Not divisible by 3 and 5

Enter a Number : 15
FIZZBUZZ

Enter a Number : 9
FIZZ

Enter a Number : 10
BUZZ
'''