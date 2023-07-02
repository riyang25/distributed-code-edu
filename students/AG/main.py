#my name is aahana
 # print means to write, triple quotes lets you add rows

x = 7 #round (3.45) rounds it to an integer
y= "by" # this is a variable with a string (text), strings need apostrophe
z="taylor swift is the best"
 # this is a comment, to print variables you need a comma + space
a= 3.1415 #this is a floating point (not an integer)

#math
x = x+5 #add 5 to x
x += 5 #literally the same thing
 #it takes the most recent one
x =x*5 #multiplication
x *= 5 #literally the same thing
x = x/5 #division
x /= 5 # literally the same thing

x = x + 5 # Add 5 to x.
x += 5    # Also adds 5 to x.
x = x * 5 # Multiplication.
x = x / 5 # Division.
x *= 5 # Also multiplication.
x /= 5 # Also division.
you = ("Alice", 21, "Pittsburgh") #this is a tuple

print (you) 
print (you[0])
print (you[1])
print (you[0], "is", you[1], "and lives in", you[2])
print (you[-1])

#this is a list
you = ["Bob", 25, "Wyoming"]
print (you)
you [1] = 26
print (you)

#comparison operators
a = 5
b = 5
print (a == b) # equal to

#inequality comparison
a = 6
b = 6
print (a != b)
# !=bang

print (a>b)
print (a>=b)

if (a==b):
    print ("A and B are equal.")
    print ("1+2")
else: print ("A and B are not equal")
password = "12345"
enter = "223456"
if (enter==password):
    print ("You have logged in")
elif (enter [0] == '1'):
    print ("You have logged in")
else: 
    print ("Wrong password")

age = input("What is your age?")
print (age) 

password = '12345'
enteredPass = input ("What's the password:")
#if (enteredPass == password) :
#   bank = input("Would you like to see your bank balance?")
#    if (bank == 'yes'):
#        print ("$100")
#    elif (bank == 'no'):
#        print ("bye!")
#else:
#print ("wrong password")

x = 10
y = 7
#while (y<=x):
    #print (y)
    #y=y+1
times = 0
while(input("what's the password")!='12345'):
    print("that is not the correct password")
    times=times+1
    if (times>5):
        break

for i in range (0,100):
    print (i)