person = {'name':'Jenn','age': '23' }
sentence = 'My name is ' + person['name'] + ' and i am ' + person['age'] + ' years old'
print(sentence)

sentence2= 'My name is {1} and i am {0} years old'.format(person['age'],person['name'])
print(sentence2)

tag='h1'
text= 'This is a headline'
print('<{0}>{1}</{0}>'.format(tag,text))

print('My name is {0[name]} and i am {0[age]} years old'.format(person))

class Person():
    def __init__(self,name,age):
        self.name =name 
        self.age = age
p1 = Person('Jenn','21')
print('{0.name} {0.age}'.format(p1))

print('{name} {age}'.format(name='Jack',age='31'))

print('{name} {age}'.format(**person))

for i in range(1,11):
    print('{:03}'.format(i))

pi=3.14159
print('Pi is equal to {:.2f}'.format(pi))

print('1MB is equal to {:,.2f}'.format(10**6))

import datetime
print(datetime.datetime(2016,9,24,12,30,45))
print('{}'.format(datetime.datetime(2016,9,24,12,30,45)))
