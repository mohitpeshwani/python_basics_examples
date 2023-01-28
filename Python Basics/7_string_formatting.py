'''
When we want to print multiple elements in a single print comment 
(1)we can simply use .format() to print out dynamic values easily 
(2) similar to r in raw string we can directly used f' ' pass the name in placeholder directly
example: 
      (1)  print("My name is {} and I am {} year old and height is {}".format(integer,floating,string))
      (2)  print(f"My name is{string} and I am {integer} year old and height is{floating})
'''

integer = 22
floating = 5.10
string = "Mohit Peshwani"
print("My name is {} and I am {} year old and height is {}".format(string,integer,floating)) #1 traditional way
print(f"My name is {string} and I am {integer} year old and height is{floating}") #2 Latest way to formatted string to print