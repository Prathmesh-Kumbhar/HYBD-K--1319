# Find the given number is Prime or Not Prime.
'''
    Prime number are those numbers which are fully divide by 1 and itself and its get the reminder will be 0.
'''

'''
Solution 1 :

    We can get a counter for count the how many number divide the given number .
    if the count is equals to 2 then its prime number otherwise its not prime number.
'''

num=12
num=11
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1

if count==2:
    print(num, "Number is Prime.")
else:
    print(num ,"Number is Not Prime.")

'''
 When the number is 11 the output is : 11 Number is Prime. 
 When the number is 12 the output is : 12 Number is Not Prime.
'''

''' 
Solution 2 :

    - We are already know the prime number is divisble by only 1 nad itself
     then we set the count is 2 and iteratons start from 2 to num.
    - Here we decrease the iteration and optimize the code
'''

num=11
count=2
for i in range(2,num):
    if num%i==0:
        count+=1

if count==2:
    print(num, "Number is Prime.")
else:
    print(num ,"Number is Not Prime.")

'''
    Solution 3 :
        -- Here we are set the count is 0 because the for loop is start from 2 then if condition is not will be true then the count will be not increase.
            so we check the count is grater than 0 then it is not prime.
        -- Or we can write count is equal to 0 then its Prime otherwise Not prime
'''
num=11
count=0
for i in range(2,num):
    if num%i==0:
        count+=1

# if count>0:
#     print(num, "Number is Not Prime.")
# else:
#     print(num ,"Number is Prime.")

if count==0:
    print(num ,"Number is Prime.")
else:
    print(num ,"Number is Not Prime")



'''
    Solution 4 :
        -- Using floor Division :
                -if any number its only divisible by its half numbers only.
                -it will goes the number of iterations with their half of the numbers. 

'''
num=11
count=0
for i in range(2,num//2):
    if num%i==0:
        count+=1

if count>0:
    print(num, "Number is NOt Prime.")
else:
    print(num ,"Number is Prime.")


'''
    Solution 5 :
        Using Break :
            - use the break keyword for minimize the number of iterations.
            - if condition is true at a first time then break the for loop and print the Number is Not prime.
'''

num=12
count=0
for i in range(2,num//2):
    if num%i==0:
        count+=1
        break

if count>0:
    print(num, "Number is NOt Prime.")
else:
    print(num ,"Number is Prime.")


# Q) Find the Prime numbers to the range of 1 to 20

for num in range(1,20):           ## It will generate the numbers from 1 to 19
    for i in range(2,num):        ## it will check the number is divisible by 2 to num-1
        if num%i==0:
            break
    else:
        print(num)

# Q) Find the Prime numbers to the range of 500 to 1000


for num in range(500,1000):    ## It will generate the numbers from 500 to 999
    for i in range(2,num):     ## it will check the number id divisible by 2 to num-1
        if num%i==0:
            break
    else:
        print(num)