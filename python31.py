def break_words(stuff):#break 分割
    """This function will break words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):#sort 排序
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):#pop 弹出第一个
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
    
def print_last_word(words):#pop(-1) 弹出最后一个
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
        
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""#拿出一个完整的句子并返回排序后的单词
    words = break_words(sentence)
    return sort_words(words)
        
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""#打印句子的第一个和最后一个单词
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
            
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""#排序单词然后打印第一个和最后一个
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)