#Arthematic operations
a = int(input("Enter first no: "))
b =int(input("Enter second no: "))

print("Sum: ", a+b)#sum of two numbers
print("Sub: ",a-b)#Subtraction of two numbers
print("Mul: ",a*b)#multiplication of two numbers
print("Div: ",a/b)#division of two numbers
print("Rem: ",a%b)#Remainder of two numbers

#Printing the type of variable
c = int(input("Enter integer value: "))
print("Type of varable: ",type(c))

d = str(c)
print("Type of variable: ",type(d))

e = input("Enter a value: ")#naturally type is str
print("Type of variable: ",type(e))

#comparison of two number
f = int(34)
g =int(80)
print("Is 34 greater than 80: ",f>g)

#print square of the number
h = int(input("Enter a number: "))

print("Square of the number: ",h**2)#we can change 2 with any number to get power easily 
print("square of the number: ",h*h)