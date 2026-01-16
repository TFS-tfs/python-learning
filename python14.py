print("How old are you?",end='')#很简单，我首先输出一个字符串
age = int(input())#接着，用input函数与用户交互，用户输入一个值，将值用int函数转换为整数，赋值给age变量
print("How tall are you?",end='')#end=''作用是让用户的交互结果不换行，显示在同一行，具体换行可见前面的python10
height = int(input())
print("How much do you weigh?",end='')
weight = int(input())
print(type(age))
print(f"So,you're {age} old,{height} tall and {weight} heavy.")#格式化字符串输出变量age,height,weight