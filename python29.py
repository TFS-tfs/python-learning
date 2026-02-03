import sys#取出sys模块
script,encoding,error= sys.argv #命令行参数赋值


def main(language_file,encoding,errors):#定义函数main,参数为文件名，编码方式，错误
    line = language_file.readline()#变量line存储文件的对象的某行内容

    if line:##if关键字 可以测试变量的真假，基于其真假运行或者不运行该代码|也就是说，如果上一行line变量存储读取到的那一行文件内容存在，则运行该代码，否则不运行
        print_line(line,encoding,errors)#函数print_line运行，参数为line,encoding,errors
        return main(language_file,encoding,errors)# 返回自身函数main,参数同上，这样就会递归调用，形成循环，除非读取到文件末尾，返回空字符串结束循环
    

def print_line(line,encoding,errors):#定义print_line函数，参数为line,encoding,errors                      DBES(decode bytes encode string)解码字节，编码字符串
    next_lang = line.strip()#变量next_lang,存储文件某行对象，用来去除行首位的空白字符串，如：换行符\n,空格等。lstrip去除左边空白字符串，rstrip去除右边的空白字符串
    raw_bytes = next_lang.encode(encoding,errors = errors)#变量raw_bytes,存储next_lang用encode方法编码后的字节序列
    cooked_string = raw_bytes.decode(encoding,errors = errors)#变量cooked,存储raw_bytes变量用decode方法解码后的字符串

    print(raw_bytes,"<===>",cooked_string)#输出raw_bytes和cooked_string，换言之，输出字节序列和对应的字符串."<===>"字符串只是为了分隔，使输出更易读


languages = open("languages.txt",encoding = 'utf-8')#变量languages,存储文件languages.txt文件对象，只读模式打开，编码utf-8

main(languages,encoding,error)#运行函数main