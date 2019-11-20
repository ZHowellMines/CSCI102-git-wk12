#   https://github.com/ZHowellMines/CSCI102-git-wk12
#   Zachary Howell
#  ​CSCI 102 – Section A
#   Week 11 - Part B

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(filename):
    with open(filename, 'r') as text:
        list_0 = []
        for line in text:
            list_0.append(line.rstrip('\n'))
    return list_0

def UpdateString(string1,string2,index_int):
    string1_list = list(string1)
    string1_list[index_int] = string2
    updated_string1 = ''.join(string1_list)
    print('OUTPUT', updated_string1)

def FindWordCount(wc_list,wc_string):
    word_count = 0
    for word in wc_list:
        if word == wc_string:
            word_count += 1
    return word_count
