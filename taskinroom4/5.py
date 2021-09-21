def rashet(file):
    global countwords
    global lenswords
    for stroka in file:
        stroka = stroka.replace('\n','')
        for slova in stroka.split():
            res = ''
            if slova.find('--') != -1:
                slova = slova.replace('--','')
            for alph in slova:
                if alph.isalpha():
                    res+=alph
                elif alph in ["'",'-'] :
                    res+=alph
            else:
                countwords+=1
                lenswords.append(len(res))

filefin = open('lesson5','w')
file1 = open('files_input4.txt')
file2 = open('files_input5.txt')
countwords = 0
lenswords = []
rashet(file1)
rashet(file2)
filefin.write(str(countwords))
filefin.write(str(round(sum(lenswords)/len(lenswords),2)))
