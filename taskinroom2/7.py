def palindrom(stroka):
    return 'Palidrom' if stroka == stroka[::-1] else 'Not palidrom'

a = input()
print(palindrom(a))
