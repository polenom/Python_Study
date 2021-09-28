text=map(int, input().split())
elem = int(input())
for num,i in enumerate(text):
    if num != elem:
        print(i, end = ' ')
