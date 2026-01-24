from sys import argv#从sys模块取出函数argv,该函数值为命令行参数
from os.path import exists#从os.path模块中取出exists函数，该函数作用为检查文件是否存在

script,from_file,to_file = argv#设定变量，值为命令行参数

print(f"Copying from {from_file} to {to_file}")#输出格式化字符串

#we could do these two on one line,how?我们可以用一行写下面的两行吗？of course！
in_file = open(from_file)#   可以简化为indate = open(from_file).read()  这等于将,建立连接和读取文件内容合并了
indate = in_file.read()

print(f"The input file is {len(indate)} bytes long")#输出格式化字符串， {len(indate)}这里的作用是输出变量indate的值对应的文本from_file的长度

print(f"Does the output file exist? {exists(to_file)}")#输出格式化字符串，exists函数检查to_file 文件是否存在
print("Ready,hit RETURN to continue,CTR-C to abort.")#输出格式化字符串，继续按回车，结束按ctrl+c
input()

out_file = open(to_file,'w')#打开to_file文件，写入模式
out_file.write(indate)#写入indate变量

print("Alright,all done.")#好了，全部完成

out_file.close()#关闭    out_file和in_file文件
in_file.close()