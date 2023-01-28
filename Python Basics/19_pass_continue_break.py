'''
Pass statement ------------> simpleset way to understand   
                              When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
break statement------------> you want to terminate a loop and skip to the next code after the loop; break will help you do that
continue statement --------> The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.

For better understanding in detail checkout this link https://www.geeksforgeeks.org/break-continue-and-pass-in-python/

'''

for i in range(0,5):
    if i==2:
        break
    elif(i==0):
        pass
    else:
        print(i)
        continue
