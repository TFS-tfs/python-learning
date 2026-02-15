from test3 import from_file_get_number
from sys import argv 
script,name,number_file = argv
print(f"Welcome to this game.{name}!\n欢迎来到这个游戏。{name}")
bear = 100000000
print("You meet a been.Been is 100000000.\n你遇见了一个灰熊。灰熊血量为100000000")
print("What could you do?你能做些什么呢？")
print('You maybe need some help?\n你或许需要一些帮助？')
print("Next,there has some ability.Maybe can help you?\嗯，这有一些技能。或许可以帮助你？")
print("Plaese choose your ability.(1~10)\n请选择你的能力。(1~10)")
found_value = from_file_get_number(number_file)
def add(number):
    return number+10000
def subtract(number):
    return number-100
def multiply(number):
    return(number*1000)
def divide(number):
    return number/5
def asmd(number):
    return divide(multiply(subtract(add(number))))
print("Please choose ability again.Which do you want?#1 or #2 or #3 or #4 or #5？请再次选择你的能力吧。你想要哪个？按下#1~5选择？")
number_again = float(input("ability能力>>> "))
if number_again == 1:
    print("Good job!Your ability has added!\n干的漂亮！你的攻击血量已经增加了！")
    result = add(found_value)
elif number_again == 2:
    print("Good job!Your ability has subtract!\n干的漂亮！你的攻击血量已经减少了！")
    result = subtract(found_value)
elif number_again == 3:
    print("Good job!Your ability has multiply!\n干的漂亮！你的攻击血量已经翻倍了！")
    result = multiply(found_value)
elif number_again == 4:
    print("Good job!Your ability has divide!\n干的漂亮！你的攻击血量已经缩倍了！")
    result = divide(found_value)
else: 
    result = asmd(found_value)
    print(f"Good job!Your ability...well,I don't konw.\n干的漂亮！你的攻击血量变为了: {result}")
if result > bear:
    print("Good!You killed the bear!\n牛逼！你单杀了熊！")
elif result == bear:
    print("Bad.You and bear all died.\n不太妙，你和熊同归于尽了。")
else:
    print("Bad.Looks that,you not luck.The bear eated your body.\n不太妙，熊吃掉了你的身体。")