from sys import argv#从sys模块取出argv 功能

script,input_file = argv#参数列表赋值给变量赋值

def print_all(f):#定义函数，参数为f
    print(f.read())#函数内容：输出f只读模式的值

def rewind(f):#定义变量，倒带，参数为f
     f.seek(0)#函数内容：移动文件针到开头

def print_a_line(line_count,f):#定义函数，参数为line_count,f
    print("current值为",line_count)
    print(line_count,f.readline())#函数内容：输出line_count,f只读某行的值
 
current_file = open(input_file)#定义变量，作用是打开input_file文件对象

print("First let's print the whole file:\n")  #输出字符串:首先让我们输出整个文件 

print_all(current_file)#运行函数，参数为current_file

print("Now let's rewind,kind of like a tape.")#输出字符串:现在让我们像倒带一样将文件指针重置到开头，就像倒磁带

rewind(current_file)#运行函数，参数为current_file

print("Let's print three lines:")#输出字符串:让我们输出三行：

current_line = 1#定义变量，值为1
print_a_line(current_line,current_file)#运行函数，参数为current_line,current_file

current_line += 1#定义新变量，值为上个变量值加1
print_a_line(current_line,current_file)#运行函数，参数为新的current_line，以及current_file

current_line += 1#定义新变量，值为上个变量值加1

print_a_line(current_line,current_file)#运行函数，参数为新的current_line,以及current_file