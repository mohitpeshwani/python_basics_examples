'''
input() method is used to input from command line interface bydefault it will be the string data type 
to convert it we can use type casting using int(),float(),complex() and no str is required as it will be by default.

    ex, 
        user =input("Enter the value") # value pring when user hit enter
        print(user) 


'''

user =input("enter the string: ")
print(user)

# Let us make the typecasting using int() and float for understanding

integer = int(input("Enter the non fractional value: "))
floating = float(input("Enter the fractional value: "))
print(f'Integer value is {integer} \nFloating value is {floating}')
