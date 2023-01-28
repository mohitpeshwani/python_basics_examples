'''
Range function creates a list till number specificed in argument
three ways of range as follow:

1) range(end) ---------------> create a list of number by default starts from 0 and till value-1 with jump(Step of +1)
    example:     range(10) # 0 1 2 3 4 5 6 7 8 9

2) range(start,end)----------> create a list of number from start and end-1 in range mentioned
    exameple:   range(1,5) # [1,2,3,4]
3) range(start,end,step)-----> create a list of numbers from start and end-1 in range mentioned with (+steps) times of jump
    exampe:     range(0,20,5) #[0,5,10,15]
 

'''
# 1st implementation
x =[range(10)]
print(x)

# #2nd implementation
# for y in range(1,5):
#     print(y)
# #3rd implementation
# for z in range(0,20,5):
#     print(z)
