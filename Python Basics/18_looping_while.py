'''

While loop best underastanding in https://www.w3schools.com/python/python


'''
# while loop executes untill it become true.
i = 1   
while i < 6:
  print(i)
  i += 1


'''
Special power to python has many languages don't allow else loop to looping statement 
but in python we can use else block with for and while loop

when condition become true in while loop it print once the else block
'''

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
