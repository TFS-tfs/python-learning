from sys import exit#从sys模块取出exit函数用于终止胸痛

def gold_room():#定义函数gold_room,无参数
    print("This room is full of gold.How much do you take?")#这个房间充满了黄金，你能拿走多少？

    choice = input("> ")# 变量variable   choice接受用户输入的值
    if "0" in choice or "1" in choice:#if 条件判断   or只有双False才为False不执行
        how_much = int(choice)#variable how_much存储被int转换为数字的choice变量存储的string
    else:#else条件判断
        dead("Man,learn to type a number.")#    dead函数执行，参数为string"孩子们，学会输入数字"

    if how_much < 50:#if 条件判断
        print("Nice,you're not greedy,you win!")#漂亮，你不贪心，你赢了
        exit(0)#结束程序
    else:#else条件判断
        dead("You greedy bastard!")#dead函数执行，参数为string"你这个贪婪的家伙!"
     
def bear_room():#定义函数bear_room,无参数
    print("There is a bear here.")#输出"这有一只熊"
    print("The bear has a bunch of honey.")#输出"这只熊有一大罐蜂蜜"
    print("The fat bear is in front of anther door.")#这只胖熊在另一扇门前
    print("How are you going to move the bear?")#你打算怎么移动这只熊？
    bear_moved = False#变量bear_moved存储布尔值False,表示熊没动
    while True:#while循环，一直执行下面的代码块
        choice = input("> ")#choice存储用户输入的值

        if choice == "take honey":#if 条件判断
            dead("The bear looks at you then slaps your face.")#dead函数执行，参数为string"熊看着你然后打你的脸"
        elif choice == "taunt bear" and not bear_moved:#elif条件判断   taunt嘲讽
            print("The bear has moved from the door")#熊从门前移开了
            print("You can go through is now.")#你现在可以通过了
            bear_moved = True#bear_moved存储布尔值True,表示熊动了
        elif choice == "taunt bear" and bear_moved:#elif条件判断
            dead("The bear gets pissed off and chews your leg off.")#dead函数执行，参数为string"熊生气了吃掉了你的脸"
        elif choice == "open door" and bear_moved:#elif条件判断
            gold_room()#gold_room函数执行
        else:#else条件判断
            print("I got no idea what that means.")#我不知道那是什么意思


def cthulhu_room():#定义函数cthulhu_room,无参
    print("Here you see the great evil Cthulhu.")#在这里你看到了伟大的邪恶克苏鲁
    print("He,it,whatever stares at you go insane,")#他，它，无论什么凝视着你，你疯了
    print("Do you flee for your life or eat your head?")#你是逃命还是吃掉自己的头？

    choice = input("> ")#choice存储用户输入

    if "flee" in choice:#if条件判断
            start()#执行start函数
    elif "head" in choice:#elif条件判断
        dead("Well that was tasty!")#执行dead函数，参数string为"嗯，那真是太好吃了！"
    else:#else条件判断
        cthulhu_room()#执行cthlhu_room函数，无参


def dead(why):#定义dead函数，一个参数
    print(why,"Good job!")#参数，干的漂亮！
    exit(0)#结束程序

def start():#定义start函数，无参
    print("You are in a dark room.")#你在一个漆黑房间里
    print("There is a door to your right and left.")#你的左右各有一扇门
    print("Which one do you take?")#你要进哪扇门？

    choice = input("> ")#choice存储用户输入
    if choice == "left":#条件判断
        bear_room()#执行函数bear_room
    elif choice == "right":#elif条件判断
        cthulhu_room()#执行函数cthulhu_room
    else:#else条件判断
        dead("You stumble around the room until you starve.")  #dead函数执行，参数为string"你在房间里跌跌撞撞知道饿死"     


start()   #执行start函数