filefinUpper = open('lesson4Upper','w')
filefinLower = open('lesson4lower','w')
file1 = open('files_input4.txt')
file2 = open('files_input5.txt')
for i in file1:
    filefinUpper.write(i.upper())
    filefinLower.write(i.lower())
for i in file2:
    filefinUpper.write(i.upper())
    filefinLower.write(i.lower())
file1.close()
file1.close()
filefinLower.close()
filefinUpper.close()
