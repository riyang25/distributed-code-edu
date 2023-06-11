#This is Maggie's file.

#This is a variable.
x = 5 #An integer.
y = 3.14 #A floating point.
z = "hi there maggie" #Text is called a "string."
print(x, y, z)

#Math
x = x + 5 #Add 5 to x
x += 5 #Also adds 5 to x
print(x)
x = x * 5 #Muliplication
x = x / 5 #Division
x *= 5 #Also multiplication
x /= 5 #Also division.
print(x)

#Boolean
are_you_alive = True
are_you_alive = are_you_alive == True #Stays true.
are_you_alive = are_you_alive == #Becomes false.
are_you_alive = not are_you_alive #If ti's true it becomes false. If it's false, it becomess true.
b1 = True
b2 = False
print(b1 and b2) #False because b2 is false. Both must be true for it to print true.
print(b1 or b2) #True because b1 is true. At least one must be true for it to print true.
print(b1^b2) # True. This is called XOR, it gives true if b1 and b2 are different.