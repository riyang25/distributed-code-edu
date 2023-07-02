#Erin Chen
print("hello")
print ("""Erin
Is
Kind
of
cold""")
x= (round((5+34+7)/3))    #hello
print(x)
#this is a variable
x=5 #an integer
y=3.14159 #A floating point
z="hi there obiwan" #text is called a string
print(x,y,z)
x=2
y="am"
z="at school"
print(x,y,z)
#math
x=x+5 #add 5 to x
x=5
print (x)
x+=5 #Same thing
you = ("Alice", 21, "pittsburgh") #This is a teple
print (you)
print (you[0])
print (you[1])
print (you[2])
print (you[0], "is", you[1], "and lives in", you[2])
print (you[-3])

#this is a list
you = ["Bob", 25, "Wyoming"]
print (you)
you[1] = 26
print (you)
#comparison operators
a = 5
b = 6
print (a == b)

a = 5
b = 10
print (a == b)

#inequality Comparison
print(a!=b)
print (a>b)
print(a<=b)
if(a==b):
    print("A and B are equal")
    print(1+2)
else :
    print("A and B are not equal")
password = "12345"
enter="12345"
if (enter==password) :
    print("you have logged in")
elif (enter[0]=='1'):
    print("you have logged in")
else:
    print("wrong password")
    
#age=int(input("what is your age?"))
#print(age)

enteredPass=input("What's the password?")
if(enteredPass==password):
    print("you have logged in")
    bank = input("do you want to see your balance")
    if(bank=="yes"):
        print("$100") 
    if(bank=="no") :
        print("bye")
x=10
y=0
while(y<x):
    print(y)
    y=y+1
times=0
while (input("what's the password?")!="12345"):
    print("that's not the correct password.")
    times=times+1
    if(times>5):
        break

if (times>5):
    print("your computer has been disabled")

