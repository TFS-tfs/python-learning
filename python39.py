from sys import argv
from python38b import C_Z_s,C_Z_s_C,C_Z_s_N,C_Z_s_A
import random
script, player_1, player_2 = argv
print(f"Welcome! {player_1} and {player_2}！\n欢迎你们!{player_1} 和 {player_2}")
print("There will have three games to win the sorce and ability.\n这儿将有三个游戏去赢得分数和能力。")
print("You and your frinde will get various game experience.But in the end,your will deul.And only one player wins.\n你和你的朋友将会体验不同的游戏，但最终，你们要决斗，而且只有一个玩家获胜。")
print("Believe me,that's interesting.\n相信我，那会很有趣。")
print("Who want to choose game at first？\n谁想先选游戏？")
print("1er or 2er?\n1号还是2号先来？")
first_input = int(input("Input #1 or #2 to choose. >>>   \n键入1或者2来选择。>>>  "))
English = None
Chinese = None
Number = None
Ability = None

def game1():    
    print("In order to fair.Please other player go away.\n为了公平，请其他的玩家先出去一会。")
    print("#1:The Chinese zodiac signs.\n1：中国生肖")
    print("#2:The war game.\n2；战争游戏")
    print("#3:The random game.\n3:随机游戏")
    second_input = int(
        input("Please choose your game by input #1 or #2 or #3.>>>  \n请按下1，2，3键来选择你的游戏.>>>  "))
    if 1 == second_input:
        print('You want to choose by yourself?\n你想自己选吗？')
        print("You want to choose by random from system?\n你想让系统随机选？")
        third_input = int(input("Tell me your answer.#3,Choose by yourself.#4,Choose by system encloding to random.\n告诉我你的回答。按3键自己选，按4键系统随机选择。"))
        if 3 == third_input:     
            C_Z_s
            C_Z_s_C
            C_Z_s_N
            zodiac_signs_choose = int(input("Please choose a zodiac signs from 1 to 12.>>>  \n请从1到12选择一个生肖。>>>  "))
            index = zodiac_signs_choose - 1
            English = C_Z_s[index]
            Chinese = C_Z_s_C[index]
            Number = C_Z_s_N[index]
            Ability = C_Z_s_A[index]
        elif 4 == third_input:
            index = random.randint(0,11)
            English = C_Z_s[index]
            Chinese = C_Z_s_C[index]
            Number = C_Z_s_N[index]
            Ability = C_Z_s_A[index]
        else:
            print("Sorry,you can't cheat.\n抱歉，别想作弊")
            third_input
        if 1 == first_input:
            print(f"Good!Man!{player_1},your choose is {English},in Chinese that named {Chinese}.In chinses zodiac signs,that number is {Number},your ability is {Ability}")
        elif 2 == first_input:
            print(f"Good!Man!{player_2},your choose is {English},in Chinese that named {Chinese}.In chinses zodiac signs,that number is {Number},your ability is {Ability}")
        else:
            print("Sorry,you can't cheat.\n抱歉，别想作弊")
            third_input  
    elif 2 == second_input:
        print("OK,your name is ")            
if first_input in (1,2):
    game1()
else:
    print("Sorry,you can't cheat.\n抱歉，别想作弊")
    first_input
def game2():
    if 1 == first_input:
        print(f"Three kingdoms you can choose:Wei,Shu and Wu.{player_1},which one do you want pick?\n这有三个王国你可以选择，魏国，蜀国和吴国，{player_1},你想选哪一个？")
    if 2 == first_input:
         print(f"Three kingdoms you can choose:Wei,Shu and Wu.{player_2},which one do you want pick?\n这有三个王国你可以选择，魏国，蜀国和吴国，{player_2},你想选哪一个？")