from sys import argv#从sys模块中取出argv列表功能

script,filename = argv#定义变量script,filename,值为argv列表中的值

txt = open(filename,encoding = 'UTF-8')#定义变量 txt,值为open函数打开filename的值

print(f"Here's your file {filename}:")#输出格式化字符串
print(txt.read())#读取并输出txt文件对象的内容
txt.close()
print("Type the filename again:")#输出字符串
file_again = input("> ")#定义变量file_again,值为input函数得到用户输入的值

txt_again = open(file_again,encoding = 'UTF-8')#定义变量txt_again,值为open函数打开file_again变量得到的值

print(txt_again.read())#读取并输出txt_again文件对象的内容
txt_again.close()