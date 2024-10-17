#Counting alphabet
name = "Piyanshu"

nameshort = len(name)#function for length
print("count:",nameshort)

#String slicing
newname = name[0:5]
print("Slice name:",newname)

print("Slice name:",name[-6:-1])
print("Slice name:",name[2:7])#this both statement give same output.

#Skipping numbers
num = "1234567890"
print("length of string: ",len(num))
print("Complet string: ",num[0:9])
print("Skiping 2 digits:",num[0:9:2])#here we skip one number form 1 to 9

alph = "abcdefghijklmnopqrstuvwxyz"
print("length of the string: ",len(alph))
print("Printing string from c to q",alph[1:17])
print("Printing string skipping two alphabet",alph[1:17:3])

#escape sequence
print("I am a good boy.\n I am a bad boy.")
