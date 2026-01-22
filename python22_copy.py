from sys import argv#从sys模块中取出argv列表功能

script,filename = argv#定义变量script,filename,值为argv列表中的值

txt = open(filename,encoding = 'UTF-8')#定义变量txt,值为open函数打开filename的值

print(f"Here's your file {filename}:")#输出格式化字符串
print(txt.read())#读取并输出txt文件对象的内容
txt.close()

