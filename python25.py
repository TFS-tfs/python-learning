# -*- coding: utf-8 -*-

# This one is like your scripts with argv
def print_two(*args):  # 定义函数print_two，参数为*args
    arg1, arg2 = args  # 将参数值赋给变量arg1,arg2
    print(f"arg1: {arg1}, arg2: {arg2}")  # 输出arg1,arg2

# ok,that *args is actually pointless,we can just do this
# 好吧，实际上那个*args是没必要的，我们仅仅需要这样做
def print_two_again(arg1, arg2):  # 定义函数以及两个参数
    print(f"arg1: {arg1}, arg2: {arg2}")  # 输出格式化字符串

# this just takes one argument 这仅有一个参数
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments 这没有参数
def print_none():  # 
    print("I got nothin'.")  # 啥也没有

print_two("Zed", "Shaw")  # 输出函数运行结果
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
