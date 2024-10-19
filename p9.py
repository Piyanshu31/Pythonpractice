#Taking 7 int(input for user and print list of seven fruits
fruit = []

f1 = input("Enter name of 1st fruit: ")
fruit.append(f1)

f2 = input("Enter name of 2nd fruit: ")
fruit.append(f2)

f3 = input("Enter name of 3rd fruit: ")
fruit.append(f3)

f4 = input("Enter name of 4th fruit: ")
fruit.append(f4)

f5 = input("Enter name of 5th fruit: ")
fruit.append(f5)

f6 = input("Enter name of 6th fruit: ")
fruit.append(f6)

f7 = input("Enter name of 7th fruit: ")
fruit.append(f7)

print(fruit)

#taking 6 student marks and print them in sorted way
student = []

s1 = int(input("Enter marks of student: "))
student.append(s1)

s2 = int(input("Enter marks of student: "))
student.append(s2)

s3 = int(input("Enter marks of student: "))
student.append(s3)

s4 = int(input("Enter marks of student: "))
student.append(s4)

s5 = int(input("Enter marks of student: "))
student.append(s5)

s6 = int(input("Enter marks of student: "))
student.append(s6)

student.sort()
print(student)

#average of all the students
s = sum(student)
avg = int(s/6)
print("Average of Student maeks: "+str(avg))#This is on way in which we make avg sting so we can concatenate the string and add avg in front of it as a string
print("Average of student marks: ",avg)

#number of zero's in following tuple
tup = (0,12,231,0,321,0,31,0,12,0,12)
c = tup.count(0)
print("Number of times zero is repeated: ",c)