# Arithmatic operation on datatypes 

# 1. Addition (+) Operator

#  Integer + Integer 
# a=10
# b=20
# print(a+b)

''' it will print addition of the two numbers 30'''
# Integer + Float 
# a=20
# b=75.5
# print(a+b)

''' The result of the integr + float value is float =>95.5'''

# Integer + Complex
# a=20
# b=75+6j
# print(a+b)

''' The result of integer + complex is first add 20+75 and print the final result is (95+6j) '''

# Integer + String

# a=20
# b="Prathmesh"
# print(a+b)

''' the result of integer + string is error because we cannot add the any string with the integer so it will print type error.'''
 
# Integer + Boolean

# a=20
# b=True
# print(a+b)

''' The result will be the in python value of boolean true is 1 then it add the value in int '''

# List + List

# a=[1,2,3,4]
# b=[4,5,6,7]
# print(a+b)

''' In this list + list will be extend the second list into the list and print one single list
    [1, 2, 3, 4, 4, 5, 6, 7]
'''

# Tuple + Tuple

a=(1,2,3)
b=(4,5,6,3)
print(a+b)

''' In this Tuple + Tuple will be add the second tuple into the tuple and print one single tuple
    (1, 2, 3, 4, 5, 6, 3)
'''
# Set + Set

# a={10,20,30,40}
# b={5,6,7,8}
# print(a+b)

''' It will print Type error because of the set addition is not possible'''

# Dictionary + Dictionary

# a={45:"Rohit",7:"Dhoni",18:"Virat"}
# b={33:"Hardik",69:"Sky",93:"Jasprit"}
# print(a+b)

''' It will Show error because we cannot add Dictionary + Dictionary'''

# 2. Substraction (-)

# Integer - Integer
# a=20
# b=10
# print(a-b)

''' It will subtract the two numbers and print result 10 '''

# Integer - Float
# a=20
# b=5.5
# print(a-b)

''' The result of integer - float will be float => 14.5 '''

# Integer - Complex
# a=20
# b=5+3j
# print(a-b)

''' First subtract real numbers (20-5) and imaginary part remains same
Result => (15-3j) '''

# Integer - String
# a=20
# b="Prathmesh"
# print(a-b)

''' It will give TypeError because subtraction is not possible between integer and string '''

# Integer - Boolean
# a=20
# b=True
# print(a-b)

''' Boolean True value is 1 so result => 20-1 = 19 '''

# List - List
# a=[1,2,3]
# b=[2,3]
# print(a-b)

''' TypeError because subtraction operation is not supported between lists '''

# Tuple - Tuple
# a=(1,2,3)
# b=(2,3)
# print(a-b)

''' TypeError because tuple subtraction is not possible '''

# Set - Set
# a={10,20,30}
# b={20}
# print(a-b)

''' In set subtraction removes common elements
Result => {10,30} '''

# Dictionary - Dictionary
# a={1:"A"}
# b={2:"B"}
# print(a-b)

''' TypeError because dictionary subtraction is not supported '''


# 3. Multiplication (*) :

# Integer * Integer
# a=10
# b=5
# print(a*b)

''' Result => 50 '''

# Integer * Float
# a=10
# b=2.5
# print(a*b)

''' Result will be float => 25.0 '''

# Integer * Complex
# a=5
# b=2+3j
# print(a*b)

''' Multiply real number with complex => (10+15j) '''

# Integer * String
# a=3
# b="Python"
# print(a*b)

''' String will repeat 3 times => PythonPythonPython '''

# Integer * Boolean
# a=10
# b=True
# print(a*b)

''' True value is 1 so result => 10 '''

# List * Integer
# a=[1,2,3]
# b=2
# print(a*b)

''' List will repeat two times => [1,2,3,1,2,3] '''

# Tuple * Integer
# a=(1,2,3)
# b=2
# print(a*b)

''' Tuple will repeat two times => (1,2,3,1,2,3) '''

# Set * Set
# a={1,2}
# b={3,4}
# print(a*b)

''' TypeError because multiplication is not supported for sets '''


# Dictionary * Dictionary
# a={1:"A"}
# b={2:"B"}
# print(a*b)

''' TypeError because dictionary multiplication is not possible '''


# 4. Division (/) :

# Integer / Integer
# a=10
# b=2
# print(a/b)

''' Division always returns float => 5.0 '''

# Integer / Float
# a=10
# b=2.5
# print(a/b)

''' Result => 4.0 '''

# Integer / Complex
# a=10
# b=2+3j
# print(a/b)

''' Result will be complex number '''

# Integer / String
# a=10
# b="Python"
# print(a/b)

''' TypeError because division between integer and string is not possible '''

# Integer / Boolean
# a=10
# b=True
# print(a/b)

''' True value is 1 so result => 10.0 '''

# List / List
# a=[1,2]
# b=[3,4]
# print(a/b)

''' TypeError because division is not supported for lists '''

# Tuple / Tuple
# a=(10,20,30)
# b=(2,4,5)
# print(a/b)

''' TypeError because division is not supported for tuple datatype '''

# Set / Set
# a={10,20,30}
# b={2,4,5}
# print(a/b)

''' TypeError because division operation cannot be performed on sets '''

# Dictionary / Dictionary
# a={1:10,2:20}
# b={1:2,2:4}
# print(a/b)

''' TypeError because division is not supported between dictionaries '''


# 5. Floor Division (//) :

# Integer // Integer
# a=10
# b=3
# print(a//b)

''' Floor division removes decimal part => result 3 '''

# Integer // Float
# a=10
# b=3.0
# print(a//b)

''' Result => 3.0 '''

# Integer // Boolean
# a=10
# b=True
# print(a//b)

''' True value is 1 so result => 10 '''

# Integer // String
# a=10
# b="Python"
# print(a//b)

''' TypeError because floor division with string is not possible '''

# List // List
# a=[10,20,30]
# b=[2,4,5]
# print(a//b)

''' TypeError because floor division operator does not support list datatype '''

# Tuple // Tuple
# a=(10,20,30)
# b=(2,4,5)
# print(a//b)

''' TypeError because floor division cannot be performed on tuples '''

# Set // Set
# a={10,20,30}
# b={2,4,5}
# print(a//b)

''' TypeError because sets do not support arithmetic operations like floor division '''

# Dictionary // Dictionary
# a={1:10,2:20}
# b={1:2,2:4}
# print(a//b)

''' TypeError because floor division is not supported between dictionaries '''

# 6. Modulus (%) :

# Integer % Integer
# a=10
# b=3
# print(a%b)

''' It prints remainder => 1 '''

# Integer % Float
# a=10
# b=3.5
# print(a%b)

''' Result => 3.0 '''

# Integer % Boolean
# a=10
# b=True
# print(a%b)

''' True value is 1 so remainder => 0 '''

# Integer % String
# a=10
# b="Python"
# print(a%b)

''' TypeError because modulus operation with string is not possible '''

# List % List
# a=[1,2]
# b=[3,4]
# print(a%b)

''' TypeError because modulus is not supported for lists '''

# Tuple % Tuple
# a=(10,20,30)
# b=(2,4,5)
# print(a%b)

''' TypeError because modulus operator does not work with tuple datatype '''

# Set % Set
# a={10,20,30}
# b={2,4,5}
# print(a%b)

''' TypeError because modulus operation is not supported for sets '''

# Dictionary % Dictionary
# a={1:10,2:20}
# b={1:2,2:4}
# print(a%b)

''' TypeError because modulus operation cannot be performed between dictionaries '''

'''
                Final chart Of The oprators operations on the fundamental and collective datatypes

| DataTypes               | +                 | -               | *                         | /            | //            | %           
| ----------------------- | ---------------   |--------------   | ------------------------- | -----------  | -----------   | ----------- 
| Integer + Integer       | ✔                | ✔               | ✔                         | ✔            | ✔            | ✔           
| Integer + Float         | ✔                | ✔               | ✔                         | ✔            | ✔            | ✔           
| Integer + Complex       | ✔                | ✔               | ✔                         | ✔            | ✔            | ✔           
| Integer + Boolean       | ✔                | ✔               | ✔                         | ✔            | ✔            | ✔           
| Integer + String        | ❌ TypeError     | ❌ TypeError    | ✔ (repeat string)         | ❌ TypeError | ❌ TypeError | ❌ TypeError 
| List + List             | ✔ (extend list)  | ❌              | ✔ (repeat list with int)  | ❌           | ❌           | ❌           
| Tuple + Tuple           | ✔ (join tuple)   | ❌              | ✔ (repeat tuple with int) | ❌           | ❌           | ❌           
| Set + Set               | ❌               | ❌              | ❌                        | ❌           | ❌           | ❌           
| Dictionary + Dictionary | ❌               | ❌              | ❌                        | ❌           | ❌           | ❌           


'''