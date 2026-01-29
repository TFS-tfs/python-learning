def add(a,b):#定义函数add,参数a,b
    print(f"ADING {a} + {b}")#函数内容，输出格式化字符串包含变量a+b的结果
    return a + b#add函数返回a+b的结果

def subtract(a,b):#定义函数subtract,参数a,b
    print(f"SUBTRACTING {a} - {b}")#函数内容，输出格式化字符串，包含变量a-b的结果
    return a-b#subtract函数返回a-b的结果

def multiply(a,b):#定义函数multiply,参数a,b
    print(f"MULTIPLY {a} * {b}")#函数内容，输出格式化字符串，包含变量a*b的结果
    return a * b#multiply函数返回a*b的结果

def divide(a,b):#定义函数divide,参数a,b
    print(f"DIVIDING {a} / {b}")#函数内容，输出格式化字符串，包含变量a/b的结果
    return a / b#divide函数返回变量a/b的结果


print("Let's do some math with just functions!")#输出字符串"让我们用函数做一些数学"

age = add(30,5)#定义变量age,值为函数add带入参数30，5返回值
height = subtract(78,4)#定义变量height,值为函数subtract带入参数78，4返回值
weight = multiply(90,2)#定义变量weight,值为函数multiply带入参数90，2返回值
iq = divide(100,2)#定义变量iq,值为函数divide函数带入100，2返回值

print(f"Age: {age},Height: {height},Weight:{weight},IQ: {iq}")#输出格式化字符串


#A puzzle for the extra credit,type it in anyway.#一个额外的谜题，无论如何输入它
print("Here's a puzzle.")#输出字符串"这有个谜题"

what = add(age,subtract(height,multiply(weight,divide(iq,2))))#定义变量what,值为带入变量作为参数依次运行函数divide,multiply,subtract,add的返回值

print("That's becomes:",what,"Can you do it by hand?")#输出字符串"结果是:"what'你能手算出来吗'