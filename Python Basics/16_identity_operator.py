'''
Identity operator is a special operator help to detemine wheather the Function is equal to or not variable/database
example:
        player ="Messi"
    case 1:  we are like to check wheather the 20 identical or not in the player variable directly we can use "is" operater (false is expected)
            print( player is "messi" ) #return false as it's M is capital

    case 2: we are like to check wheather the 20 identical the list directly we can use  "is not" operator  (true is expected)
            print( player is not  "messi")  #return true as it's M isn't matching 
'''

player ="Messi"
print( player is "messi" ) #return false as it's M is capital
print( player is not  "messi") #return true as it's M isn't matching 
