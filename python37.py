from sys import argv#取出列表
script,name = argv#赋值
print(f"Welcome to this loop_game,{name}！")#输出欢迎
len_name = len(name)#存储名字长度
print("How long your name,this script will rounds times.")#输出 你的名字多长，这个脚本就会循环几次
def while_loop():#定义函数
    numbers = []
    i = 0
    while i < len_name:#布尔判断
        print(f"At the top i is {i}")#输出 在顶部，i是{i}
        numbers.append(i)#将i添加到空列表numbers中

        i += 1#变量增加
        print("Numbers now: ",numbers)#输出现在numbers是: numbers
        print(f"At the bottom i is {i}") #bottom 底部


    print("The numbers: ")#输出最终列表numbers

    for num in numbers:#取出numbers列表的元素按次序赋值给num变量直到取完为止
        print(num)#打印变量
while_loop()#执行函数
def exercise_function():
    numbers_1 = []
    i_1 = 0
    while i_1 < len_name:
        print(f"At the top i is {i_1}")
        numbers_1.append(i_1)

        i_1 += 1
        print("Numbers now: ",numbers_1)
        print(f"At the bottom i_1 is {i_1}")

    print("The numbers_1: ")
    for num_1 in range(0,12):
        print(num_1)
exercise_function()