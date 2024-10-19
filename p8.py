#Tuple in python
num = (1,21,3,12,3,43,3,21,3)#tuple is immutable just like string
print(num)
print(num[0])

'''num[0]=121
print(num[0]) This show error as tuple is immutable'''

#method in touple
no = num.count(3)
print(no)#count no of times value is repeated

i = num.index(12)
print(i)

l = len(num)
print(l)

num2 = (2,3,2,4,32,43)
concatenation = num + num2
print(concatenation) #new tuple name concatenation having all  elements of tuple num and num2

#Repeat tuple num 3 time in repeated tuple
repeated = num *3 
print(repeated)