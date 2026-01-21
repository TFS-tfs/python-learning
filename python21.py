from sys import argv #从sys模块中取出argv功能

script,user_name = argv#定义变量script,user_name       script脚本
prompt = '> '#定义变量prompt,值为字符串'> '           prompt提示符

print(f"Hi {user_name},I'm the {script} script.")#输出格式化字符串
print("I 'd like to ask you a few questions")#输出字符串
print(f"Do you like me {user_name}?")#输出格式化字符串
likes = input(prompt)#定义变量likes,值为用户输入在>之后的内容，注意，该值为字符串，而非数字，需要的话要进行数据转化，如:likes  = int(input(prompt))

print(f"Where do you live {user_name}?")#同上
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright,so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.Nice.
     """)#好的，你说了  来表示是否喜欢我。你住在  ，不太确定那是哪。你有一台  电脑。漂亮，
