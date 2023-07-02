password = "ue38s7"
password2 = "yr834i"












incorrect = 0
enteredPass = input("Password: ")

if(enteredPass == password):
    enteredPass2 = input("Second Password: ")
    if(enteredPass2 == password2):
        name = input("Enter your name: ")
        print("Access Granted. Welcome " + name + "! Opening file test.python.file@github")
        print("|     | 0%")
        print("|=    | 20%")
        print("|==   | 40%")
        print("|===  | 60%")
        print("|==== | 80%")
        print("|=====| 100%")
        x = int(input("Enter in a positive integer:"))
        y = int(input("Enter in a positive integer less then the previous number:"))
        while(y <= x):
            print(y + x)
            y +=2
            x += 1

    elif(enteredPass2 != password2):
        print("Access Denied, Wrong Password.")
        incorrect += 1
else:
    print("Access Denied, Wrong Password.")
    incorrect +=1