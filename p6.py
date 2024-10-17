#take name from user and print good afternoon and your name
name = input("Enter your name: ")

print(f"Good afternoon {name}")
print("Good afternoon "+name)

#make changes in letter
letter = '''Your <name>
You are selected!
<date>'''
print(letter.replace("<name>","Piyanshu").replace("<date>","10 oct 2024"))