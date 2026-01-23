from sys import argv#从sys模块取出argv列表功能

script,filename = argv#将命令行参数argv的值赋值给变量script,filename

print(f"We're going to erase {filename}.")#输出格式化字符串“我们将要清除filename”
print(f"If you don't want that,hit CTR-C (^C).")#输出格式化字符串“如果你不想要那个，按下ctrl+c键”
print("If you do want that,hit RETURN.")#输出字符串“如果你想要那个，按下回车键”

input("?")#input提示“？”与用户交互

print("Opening the file...")#输出字符串“打开文件......”
target = open(filename,'w+',encoding = 'UTF-8')#设置变量target,值为右边open函数打开的文件对象。  或者可以说，以写入模式打开文件filename。如果文件存在，则清除，然后重头写入；如果文件不存在，则创建文件。
#W+模式也会和w模式一样清空文件，创建文件，不过在下面用seek(0)后不用再打开文件倒是好事情
print("Truncating the file.Goodbye!")#输出字符串“清除文件，再见！”
target.truncate()#清除文件     target:目标

print("Now I'm going to ask you for three lines.")#输出字符串“现在我将要问你三行内容”

line1 = input("line 1:")#设置变量line1-3,值分别对应为input与用户交互，用户输入的值
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")#输出字符串“我将要写入这些在文件里”

target.write(f"""{line1}
{line2}
{line3}
             """)
print("And finally,we close it.")#输出字符串“最后，我们关掉它”
target.seek(0)
print(target.read())
target.close()