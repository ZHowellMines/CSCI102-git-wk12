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