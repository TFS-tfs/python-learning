types_of_people = 10  #定义变量type_of_people并将10赋值给它      
x = f"There are {types_of_people} types of people."#定义变量x,并将含有变量types_of_people的格式化字符串f"There are {types_of_people} types of people."赋值给它
#上面一行是新方法f-string，用来给字符串中插入变量
binary = "binary"#定义变量binary,并将"binary"赋值给它     binary 二进制
do_not = "don't"#定义变量do_not,并将"don't"赋值给它
y= f"Those who know {binary} and those who {do_not}."#定义变量y,并将含有变量binary和变量do_not的格式化字符串f"Those who know {binary} and those who {do_not}."赋值给它
print(f"I said:{x}")#binary  二进制}")#打印格式化字符串"I said:{x}")
print(f"I also said:'{y}'")#打印格式化字符串"I also said:'{y}'")

hilarious = False   # 定义一个布尔型变量hilarious，值为false,
joke_evaluation = "Isn't that joke to funny?!{}"#定义一个字符串变量jole_evaluation,值为"Isn't that joke to funny？！{}"
print(joke_evaluation.format(hilarious))#这里用的是format()方法将参数false插入上面的占位符{}中，算是比较传统的办法

w = "This is the left side of..."#定义变量w,值为"This is the left side of..."
e = "a string with a right side."#定义变量e,值为"a string with a right side."

print(w+e)#输出变量w+e的结果