'''
1. you have ine list of students marks .
    create a two sub lists for even and odd marks students.
'''
student_marks=[88,55,45,15,12,45,75,15,76,78,99,98,95,75,25,55,66,77,96,94,88,78,56,46]
even_marks=[]
odd_marks=[]

for i in student_marks:
    if i%2==0:
        even_marks.append(i)
    else:
        odd_marks.append(i)
print("Even Marks List is : ",even_marks)
print("ODD Marks List is : ",odd_marks)

'''
    It will print the 2 sub lists of even marks and odd marks
    Even Marks List is :  [88, 12, 76, 78, 98, 66, 96, 94, 88, 78, 56, 46]
    ODD Marks List is :  [55, 45, 15, 45, 75, 15, 99, 95, 75, 25, 55, 77]
'''
