'''
Arithmetic Operators
'''
print(2+1) #
print(2-1)
print(4/2)
print(4%3)
print(2**4)

'''
Logical Operators

(Used to return boolean like switch on and off)

'''

print( 6>2  )
print( 6>=2 )
print( 6<2  )
print( 6<=2 )
print( 6==2 )
print( 6!=2 )

'''
Conditional Operators

(Used to return boolean like switch on and off)

'''
print( 2==2 and 2>1 )
print( 2==2 or 2>1 )
print( not 2==2 )

'''
Bitwise Operators

(Logical implementation on bit level)

'''
print( ~1   )
print( 1&2  )
print( 1|2  )
print( 1^2  )
print( 1<<2 )
print( 2>>1 )

'''
Identity and Membership Operators
(Special operator to compare the identity wheater they are from the same object)--> Identity Operator --> is / is not
(Special operator to check wheather the variable is belong to a group or not)--> Membership operator --> in / not in

(i) is 
(ii) is not
(iii) in
(iv) not in
'''
x= 20
i =[10,20,30,40,60,70]

print(x is 20)
print(x is not 20)
print(x in i)
print(x not in i)

'''
Assignment Operators( = )

To assign the memory/allocate the resources to the variable,objects
'''
x = 20
i[1] += 10 #shorthand techinque to perform any arithmetic opertor with this
x /= 2
print(x)
print(i)
