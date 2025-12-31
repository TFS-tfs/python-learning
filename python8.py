name = 'Zed A. Shaw'
age  =  35 # not a lie没骗人
inch_to_cm =2.54    
pound_to_kg=0.4536
height  =  74*inch_to_cm # inches英寸
weight  =  180*pound_to_kg  #lbs磅
eyes   =  'Blue'
teeth  =   'White'
hair  =  'Brown'
print(f"Let's talk about {name}.")          #我们来聊一下   我的名字
print(f"He's {height} centimeter tall.")            #他的身高    英寸
print(f"He's {weight} kg heavy.")           #他的体重     磅
print("Actually that's not too heavy.")             #事实上没有多重
print(f"He's got {eyes} eyes and {hair} hair.")  #他有   色的眼睛和  色的头发
print(f"His teeth are usually {teeth} depending on the coffee.")   #他的牙齿通常是   色取决于喝了多少咖啡
#this line is tricky,try to get ie exactly right    这一行需要注意，要尽力确保完全正确
total = age + height + weight             
print(f"If I add {age}, {height}, and {weight} I get {total}.")  #如果我把 ， ， 和  ，  加起来，我会得到    。
#厘米Centimeter    千克Kilogram 
#1 lnch =2.54 centimeter   1 pound≈0.4536kg
