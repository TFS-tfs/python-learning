age = input("How old are you?")
height = input(f"You 're {age}? Nice.How tall 're you?")
weight = input(f"How much do you weigh?")

print(f"So,you're {age} old,{height} tall and {weight} heavy.")#input函数可以套用格式化字符串，可以直接将一个字符串用作提示符
#14.py是用print函数输出字符串用来提问用户，接着用input函数等待用户输入以达成和用户交互的目的。
#这个则是更简单，直接用input函数呈现给用户一个字符串或者是格式化字符串来当作提示符以达成与用户交互的目的。

#那么，我们可以尝试：
a = int(input("5+5等于几？"))
s = int(input(f"可以套几层？{a}层。(随便给个数字)"))
d = a/5+s
print(f"{a}层太多了，我们尝试套{d}层就好啦。")
#我们当然可以在格式化字符串里面调用input，但是会有以下问题：
#1，语序混乱  2，可能被执行恶意代码