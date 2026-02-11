people = 30 #定义变量people，存储30，以下两个同理
cars = 40#汽车或小轿车
trucks = 15#卡车
if cars > people:#转换为布尔判断，如果cars > people 为真，则执行下面的代码
    print("We should take the cars.")#输出字符串"我们应该开汽车去"
elif cars < people:#转换为布尔判断，否则如果(排除if情况下:)cars < people为真，则执行下面的代码
    print("We should not take the cars.")#输出字符串"我们不可以开汽车去"
else:#转换为布尔判断，否则(排除以上if和elif的情况下:)为真，则执行下面的代码
    print("We can't decide.")#输出字符串"我们无法决定"
if trucks > cars:#同上，同理
    print("That's too many trucks.")#太多卡车了
elif trucks < cars:
    print("Maybe we could take the trucks.")#也许我们可以坐卡车去
else:
    print("We still can't decide.")#我们依然无法决定
if people > trucks:
    print("Alright,let's just take the trucks.")#好吧，我们就开卡车吧
else:
    print("Fine,let's stay home then.")#好吧，呆在家里吧