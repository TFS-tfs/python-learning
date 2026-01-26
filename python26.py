def cheese_and_crackers(cheese_count,boxes_of_crackers):#定义函数cheese_and_crackers,参数为份奶酪，盒饼干
    print("cheese_count",cheese_count,"boxes_of_crackers",boxes_of_crackers)
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")#孩子们，够开party了
    print("Get a blanket.\n")#拿条毯子来
    print(">>>> exit this function.")

print("We can just give the function numbers directly:")#我们可以直接给函数传递数字作为参数，而不通过中间的变量
cheese_and_crackers(20,30)


print("OR,we can use variables from our script: ")#我们也可以使用变量在脚本中
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)


print("We can even do math inside too:")#我们也可以在里面做数学
cheese_and_crackers(10+20,5+6)

print("And we can combine the two,variables and math:")#我们可以把变量和数学加起来

cheese_and_crackers(amount_of_cheese +100,amount_of_crackers +1000)