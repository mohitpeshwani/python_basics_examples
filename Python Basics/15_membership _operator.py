'''
Membership operator is a special operator help to detemine wheather the Function is available or not in the database/ Data structure  in which we are looking
example:
        list1=[10,20,40,506,707,77]
    case 1:  we are like to check wheather the 20 available or not in the list directly we can use "in" operater (true is expected)
            print( 20 in list1) #return true

    case 2: we are like to check wheather the 20 available or not in the list directly we can use  "not in" operator  (false is expected)
            print(20 not in list1)
'''

list1 = [10,20,40,506,707,77]
print(20 in list1) #expectation to be true as it's available in the list
print(20 not in list1) #expectation to be false as it's available in the list
