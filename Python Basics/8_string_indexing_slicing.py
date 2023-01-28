'''
String is the sequence of characters.
To access the individual character we can use the index numbers in string to access them and check them.
        ex, name = "Mohit Peshwani"
            print(name[2])  #o

Slicing is to create a substring out of the main string 
        ex, name= "Mohit Peshwani"
            print(name[2:5]) #hit
Another way to do substring the string is using substring function
        ex, name= "Mohit Peshwani"
            print(name.substring(2,5))


'''

name = "Mohit Peshwani"
print(name[2])
print(name[-12]) #negative indexing to get element from end



name = "Mohit Peshwani"
print(name[2:15]) #
print(name[0:len(name):3])
