the_count = [1,2,3,4,5]#定义变量存储列表
fruits = ['apples','oranges','pears','apricots']#同上   # apricots杏子
change = [1,'pennies',2,'dimes',3,'quarters']#同上

#this first kind of for-loop goes through a list 第一种for循环，遍历列表
for number in the_count:#从the_count列表按顺序取出每种元素，分别赋值给number变量
    print(f"This is count {number}")#每次遍历列表取出变量并赋值后输出格式化字符串"这是数字 {number}""

#same as above 同上
for fruit in fruits:           #这里的fruit可以是任何名字，反正都只是存储列表里面变量的东西罢了
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too也可以遍历混合类型的列表
#notice we have to use {} since we don't know what's in it  注意因为不知道里面是什么类型，所以用 {} 来格式化
for i in change:
    print(f"I got {i}")

    #we can also build lists,first start with an empty one
elements = []#定义elements存储空列表

#then use the range funcion to do 0 to 5 counts然后使用range函数进行0~5的计数
for i in range(0,6):
    print(f"Adding {i} to the list.")
#append is a function that lists understand append是列表支持的一个函数，用于在末尾添加元素
    elements.append(i)

#now we can print them out too现在我们可以把它们打印出来
for i in elements:
    print(f"Element was: {i}")
    