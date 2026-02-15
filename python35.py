print("""Your enter a dark room with two doors.
Do you go through door #1 or door #2?""")#输出字符串"你进入了一个漆黑的房间，有两扇门.你选1还是2？"

door = input("> ")#等待用户交互

if door == "1":#如果用户选1号门
    print("There 's a giant bear here eating a cheese cake.")#输出字符串"这有一只巨大的熊在吃奶酪蛋糕。"
    print("What do you do?")#输出字符串"你做什么?"
    print("1.Take the cake.")#输出字符出串"1.拿走蛋糕"
    print("2.Scream at the bear.")#输出字符串"2.对熊尖叫"

    bear = input("> ")#等待用户交互

    if bear == "1":#如果用户选1
        print("The bear eats your face off.Good job!")#输出字符串"熊吃掉了你的脸.干的漂亮！"
    elif bear == "2":#如果用户选2
        print("The bear eats your legs off.Good job!")#输出字符串"熊吃掉了你的腿，干的漂亮！"
    else:#如果用户输出别的
        print(f"Well,doing {bear} is probably better.")#输出格式化字符串"好吧，选 {bear} 可能更好"
        print("Bear runs away.")#输出字符串”熊跑了"

elif door == "2":#否则如果用户选2号门
    print("You stare into the endless abyss at Crhulhu's retina.")#输出字符串"你凝视无尽深渊，克苏鲁的视网膜."
    print("1.Blueberries.")#输出字符串"1.蓝莓"
    print("2.Yellow jacket clothespins.")#输出字符串"黄色夹克衣夹"
    print("3.Understanding revolvers yelling melodies.")#输出字符串"理解左轮手枪旋律"

    insanity = input("> ")#等待用户交互
    if insanity == "1" or insanity == "2":#如果用户选1或者2
        print("Your body survives powered by a mind of jello.")#输出字符串"你的身体幸存下来，但思想像果冻一样"
        print("Good jobs!")#输出字符串"干的漂亮！"
    else:#否则
        print("The insanity rots your eyes into a pool of muck.")#输出字符串"疯狂让你的眼睛烂成一滩泥浆"
        print("Good job!")#输出字符串”干的漂亮！"


else:#否则
    print("You stumble around and fall on a knife and die.Good jobs!")#输出字符串"你跌跌撞撞，摔倒在一把刀上死了。干的漂亮！")
