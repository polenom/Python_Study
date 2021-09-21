filefinNum = open('lesson3Num','w')
filefinAlpha = open('lesson3Alpha','w')
file1 = open('files_input3.txt')
for i in file1:
    if i[:-1].isdigit():
        filefinNum.write(i)
    elif i[:-1].isalpha():
        filefinAlpha.write(i)
filefinNum.close()
filefinAlpha.close()
