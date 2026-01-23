from sys import argv
script,file = argv
print("We're going to look at some files and truncate some files. ")
print("Are you ready?")
input("If you are ready,please hit ENTER.Or you aren't,please hit CTRL+C.")
print(f"We 're turncating {file}.")
target = open(file,'w',encoding = 'UTF-8')
X = "Do you want to write something?"
Y = "Answer 'Yes' or 'No'."
print(X)
C = input(Y)
print(f"I know.You answer {C}.")
First_line = input('This is first line:> ')
Second_line = input('This is second line:> ')
Third_line = input('This is third line:> ')
target.write(First_line+"\n")
target.write(Second_line+"\n")
target.write(Third_line+"\n")
target.close()