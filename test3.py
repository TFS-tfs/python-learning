def from_file_get_number(number_file):
    number= float(input("number选能力吧:>>> "))
    f = open(number_file,'r')
    current_line = 1
    found_value = None
    for line in f:
        if current_line == number:
            found_value = float(line.strip())
            break
        else:
            current_line += 1
    f.close()
    if found_value is None:
        print("Don't have this ability.Man!Please choose again.\n没这个能力，孩子!重新选吧。")
        from_file_get_number(number_file)
    else:
        print(f"Good!Your ability is {found_value}.Can you kill the bear?\n好样的！你的攻击和血量为 {found_value}。你能杀死熊吗？")
    return found_value
    
    