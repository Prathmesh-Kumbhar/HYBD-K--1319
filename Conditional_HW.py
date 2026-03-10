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

