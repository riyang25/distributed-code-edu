# Comparison Operators
a = 5
b = 5
# print(a == b) # Equality

# print(a != b) # Not equal to.

print(a > b) # Is a greater than b.
print(a < b) # Is a less than b.
print(a>=b) # greater than or equal to
print(a<=b) # less than or equal to 

if (a>b) :
    print("A and B are equal.")
    print(1+2)
else:
     print("A and B are not equal")
password = "12345"

enter = "123456"
if (enter==password) :
    print("You have logged in")
elif (enter[0]=='1') :
    print("you have logged in")
else: 
    print("wrong password")

age = input("What is your age?")
print(age)

#enteredPass = input("What's the password?")
#if (enteredPass == password) :
#    bank = input("Would you like to see your bank balance")
#       print("$100")
#    elif (bank=="no"):
#        print("bye")
x=10
y=0
while (y<x) :
    print(y)
    y=y+1
times = 0
while(input("what's the password")!= "12345"):
    print("that is not the correct password.")
    times= times+1
    if (times>5):
        break

if(times>5):
    print("your computer has been disabled")

for i in range(0,100) :
    print(i)
"""
Symbols in Programming

! bang
# pound
% modulo
^ carat
& amperpsand
* asterisk
() parenthesis
[] brackets
{} curly braces
"""
