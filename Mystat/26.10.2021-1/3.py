def myCount(Mytuple, key, newword):
    return tuple( newword if i == key else i for i in Mytuple)
x = ('banana', 'for','apple','apple-fdffd')
print(myCount(x,*input().split()))
