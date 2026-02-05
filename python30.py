print("Let's practice everying.")#输出("让我们来练习所有内容")
print('You\'d need to know \'bout escapes with \\ that do:')#输出('你需要了解关于使用反斜杠\\的转义字符，它们可以做到:')
print('\n newlines and \t tabs')#输出('\\n 换行 和 \\t制表符‘)

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""#诗 = """
#\t美好的世界
#逻辑如此根深蒂固
#无法分辨\\n爱的需求
#也无法理解来自直觉的激情
#并要求一个解释
#\\n\\t\\t而那里本没有解释
#"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6#定义变量 five = 10-2+3-6
print(f"This should be five:{five}")#输出格式化字符串，f-string方法

def secret_formula(started):#定义 函数secret_formula秘密公式(started为参数):
    jelly_beans = int(started * 500)  # 豆子，确保为整数
    jars = jelly_beans // 1000  # 罐子（整数除法）
    crates = jars // 100  # 箱子（整数除法）
    return jelly_beans, jars, crates


start_point = 10000
beans,jars,crates = secret_formula(start_point)#函数运行返回值赋给三个变量,就是拆分元组(jelly_beans,jars,crates)分别赋值给变量
#这里还体现了函数内部的变量名和函数外部接受它的变量beans可以不同，体现了变量作用域的概念
#remember that this is another way to format a string#记住，这是格式化字符串的另一种方式
print("With a starting point of: {}".format(start_point))#输出("起始点为{}。格式化(起始点)")
#it's just like with an f"" string#这就像使用f""字符串一样
print(f"We'd have {beans} beans,{jars} jars,and {crates} crates.")#输出(f"我们将有{beans}个豆子，{jars}个罐子，和{crates}个板条箱)

start_point = start_point / 10

print("We can also do that this way:")#输出("我们也可以这样做:")
formula = secret_formula(start_point)#变量存储运行secret_formula参数strat_point的结果，也就是说:带入参数start_point后formula = (jelly_beans,jars,crates)
#this is an easy way to apply a list to a format string#这是一种简单的方法将列表应用到格式化字符串
print("We 'd have {} beans,{} jars,and {} crates.".format(*formula))#类似from sys import argv的解包赋值，不过这里是自动的，*就是自动作用
