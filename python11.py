formatter = "{}{}{}{}"#定义一个字符串变量formatter,他的值是{}，{}，{}，{}。这是一个模板，可以按顺序在{}内填入对应的值。

print(formatter.format(1,2,3,4))#对应填土1，2，3，4在前面变量formatter的值{}{}{}{}中
print(formatter.format("one","two","three","four"))#同上
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Try your",   #尝试你的
    "Own text here",#自己的文本
    "Maybe a poem",#也许是一首诗
    "Or a song about fear"#或者一首关于恐惧的歌
))#注意，这里输出结果不会换行，要换行有四种办法：
#1，formatter="{}\n{}\n{}\n{}\n"    2,添加"""三引号    3，formatter=...这部分不变，在后面具体部分添加\n,如：
#print(formatter.format(1\n,2\n,3\n,4\n))              4多个print函数输出，因为print函数默认换行