#list in python
student = ["Rohan","25","9th","450/600"]
print(student)
print(student[0])
student[0]="Vishwa"#Unlike string list are mutable
print(student[0])

#slicing list
print(student[1:3])

#method in string
student.append("2nd in boy")
print(student)#list itself is changed

list = [1,21,221,11,20,122]
list.insert(4,231)#inserting 231 in 4th postion in list
print(list)
list.sort()#sort modified list in ascending order
print(list)
list.reverse()#reverse the sorted list
print(list)

#Making new list without harming the previous list
l2 = list.insert(3,321)
print(l2)