people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")#太多猫了！世界完蛋了！

if people > cats:
    print("Not many cats! The world is saved!")#没有多少猫！世界得救了！
if people < dogs:
    print("The world is droolde on!")
if people > dogs:
    print("The world is dry!")
dogs += 5
if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People ate dogs.")
if not(1 == 2 and 3 >= 3 == 3):
    print(False)
if 1 != 2 or 3 < 3 == 3:
    print(True)