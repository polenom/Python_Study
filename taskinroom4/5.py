def rashet(file):
    global countwords
    global lenswords
    for stroka in file:
        for slova in stroka.split():
            res = ''
            if len(slova) == 1 and  slova.isalpha():
                countwords+=1
                lenswords.append(1)
                continue
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
countwords = 0
lenswords = []
filefin = open('lesson5','w')
with  open('files_input4.txt') as file1:
    with open('files_input5.txt') as file2:
        rashet(file1)
        rashet(file2)
filefin.write(str(countwords)+'\n')
filefin.write(str(round(sum(lenswords)/len(lenswords),2)))
filefin.close()
