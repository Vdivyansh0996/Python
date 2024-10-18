student={'name':'Deev','age':19,'courses':['Maths3','Optics']}
print(student['courses'])
student['phone']='98'
print(student.get('phone','Not found'))
student.update({'name': 'Harry','age':'14','phone':'57'})
print(student)
age =student.pop('age')
print(age)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for key,value in student.items():
    print(key,value)