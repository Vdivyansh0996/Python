courses = ['math3','Optics','Emt-1','POE']
courses.append('CMech')
courses.insert(2,'EVS')
print(courses)
courses2= ['Art','Compsci']
courses.insert(0,courses2)
courses.extend(courses2)
print(courses)
courses.remove(courses2)
pop=courses.pop()
print(courses)
print(pop)
num=[3,6,8,2,5,9]
#num.sort(reverse=True)
#print(num)
num.reverse()
print(num)
sorted(num)            #instead of sort method, sort function can be used
print(num)             #creates a new list
print(min(num))
print(sum(num)) 
print(max(num))
print(courses.index('Optics'))
print('math3' in courses)
for index,course in enumerate(courses,start=1):
    print(index,course)
courses_str=' - '.join(courses)# list to string
print(courses_str)
new_list=courses_str.split(' - ')
print(new_list) #lists are mutable and tuples are not

courses2=courses
print(courses2)
courses[0]='Math3'
print(courses2) #courses2 points to courses
#sets
set = {'math3','Optics','Emt-1','POE','Optics'} # duplicates will be removed
print(set)
print('math3' in set)   #membership test,can do with list and tuples but sets are optimized for it
set2 = {'math3','Optics','Arts','design'}
print(set.intersection(set2))
print(set.union(set2))
print(set.difference(set2))
empty_set=set()
print(empty_set)