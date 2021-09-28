text = input().split()
for i in range(1, len(text)):
    if (text[i][0] == '-' and text[i - 1][0] == '-') or (text[i][0] != '-' and text[i - 1][0] != '-'):
        print(text[i-1], text[i])
        break
    
