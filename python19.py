x = "这是一个混合型练习" 
y = "什么样的练习？"
z = "一个关于字符串变量，for-string方法，format方法，argv,input混合的练习"
print(x)
print(y)
print(z)
q = input("要开始游戏吗？")
print(f"好的，我们{q}游戏")
gx = int(input("首先，这是一个长方体面积与体积计算器，计算结果会取整数近似值，请输入长度length:"))
length = (f"好的，我知道了，长方体长度length为:{gx}")
gy = int(input("接着，请输入宽度width:"))
width = (f"长方体宽度wide为:{gy}")
gz = int(input("最后，请输入高度height:"))
height = (f"长方体高度height为:{gz}")
print(length,width,height)
s = input("开始计算吗？")
print(f"好的，我们{s}计算")
area = 2*(gx*gy+gx*gz+gy*gz)
volume = gx*gy*gz
print("所以，该长方体的面积为{}，该长方体的体积为{}".format(area,volume))
print("哈哈，很麻烦吧，而且还不准确。所以下一个练习将简化流程，请在python20.py运行时直接给出长宽高的参数")