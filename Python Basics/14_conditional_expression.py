'''
condition cases help out to handle if not this case then perform another task(Ternary operations)

(1) if condtion ------------------> only check wheater to perform it or not (Logical and conditonal operators are used here to understand to manage the logic)
(2) if else condition ------------> If first condition doesn't satisfied then perform the default operation i.e(else) block
(3) if elif else condition--------> If there are more than 2 conditions we can perform the menu driven using if else ladder(in other languages) as python doesn't support the switch cases
(4) nested if else condtion-------> For the complex condition we can use this (Best practice to avoid this and use logical operator to perform if ekif else)


'''
# IF conditions (1)
# lets check for if condition for true condtion

x = 10
if 10 == x:
    print("1st if condition works")

# lets check if condition for false condition

y = "mohit"
if "Mohit" in y:
    print("1st if condition doesn't works")

# If else conditions (2)
# let check for if else condition for true condition if block will executed

x = 10
if 10 == x:
    print("2st if condition works")
else:
    print("Sadly not works")

# lets check if else condition for false condition else block will executed

y = "mohit"
if "Mohit" in y:
    print("sadly not works")
else:
    print("2nd condtion for false works and else executing")

#If elif else condition (3)
## let check for if else condition for true condition if block will executed
x=10 
y=20
if x==10 and y==x:
    print("sadly not works")
elif x==10 and y==20:
    print("3rd conditon for true works in if or elif block")
else:
    print("sadly not works")

#(4)nested if else condtion
#let check nested if else for true condtion
name ="Mohit"
age =22
if name is "Mohit":
    if age is 22:
        print("Details matched")
    elif age>18:
        print("Details miss but eligible for vote")
    else:
        print("Details mismatch")
else:
    print("Name is not proper")
    

#let check nested if else for false condtion 
name ="mohit"
age =22
if name is "Mohit":
    if age is 22:
        print("Details matched")
    elif age>18:
        print("Details miss but eligible for vote")
    else:
        print("Details mismatch")
else:
    print("Name is not proper")
    
