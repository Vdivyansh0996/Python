message='stokes\' World'
message1="Stokes' World"
message2="""Donald said the N
word"""
print(message) 
print(message1)
print(message2)
print(len(message2))
print(message2[16])
print(message1[0:7]) #first index is inclusive while the second is not
print(message[:6])
print(message2[16:])
print(message1.upper())
print(message2.lower())
print(message.count("World")) #takes string as an argument 
print(message2.count("d"))
print(message1.find("World")) #W is at 8th index
message1.replace("World","Universe")
print(message1) #its not replacing world in place, rather its creating a new string with the replacements
print(message1.replace("World","Universe"))
message1=message1.replace("World","Universe") 
print(message1)
greeting="Hello"
name="Cosby"
message3='{}, {}. Welcome!'.format(greeting,name) #{} are place holders #greeting + ', ' + name + '. Welcome!'
print(message3)
print(f'{greeting}, {name.upper()}! Enjoy your meal.')
#print(dir(message)) # displays all the atributes and methods available
#print(help(str)) #works on class
print(help(str.find))
x=10
print(x)