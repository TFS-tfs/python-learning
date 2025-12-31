height_cm = int(input("请输入身高(cm): "))
weight_kg = int(input("请输入体重(kg): "))
height_m  = height_cm/100
height_squared = height_m**2
bmi = weight_kg / height_squared
print(f"身高：{height_cm}厘米，也就是{height_m} 米")
print(f"身高平方：{height_squared:.2f}平方米")
print(f"体重:{weight_kg}公斤")
print(f"BMI指数:{bmi:.2f}")
if  bmi < 18.5: 
    print("瘦成猴了，多吃点，快发育")
elif bmi <24:
    print("正常发育")
elif bmi <28:
    print("稍微吃多了，少吃点")
else:
    print("别刷吃了孩子，你一个人吃了五个人的经济了")