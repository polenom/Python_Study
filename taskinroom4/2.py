filefin = open('lesson2','w')
file1 = [ int(i[:-1]) for i in open('files_input3.txt') if i[:-1].isdigit()]
filefin.write(str(len(file1))+'\n')
filefin.write(str(max(file1))+'\n')
filefin.write(str(min(file1))+'\n')
filefin.close()
