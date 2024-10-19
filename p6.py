#take name from user and print good afternoon and your name
name = input("Enter your name: ")

print(f"Good afternoon {name}")#f is needeed in this to print string
print("Good afternoon "+name)

#make changes in letter
letter = '''Your <name>
You are selected!
<date>'''
print(letter+"\n")
print(letter.replace("<name>","Piyanshu").replace("<date>","10 oct 2024"))

#Double space in string
names="My name  is Piyanshu"
print(names.find("  "))
print(names.replace("  "," "))#op as My name is piyanshu
print(names)#String are immutable which means that you cannot change them be running fuction on them

#formating letter by escape sequence
letters="This is the python program.\n\tThanks for writing it.."
print(letters)