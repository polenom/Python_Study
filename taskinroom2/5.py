def rangeAandB(mylist,AB):
    return [ i for i in mylist if sorted(AB)[0] <= i <=sorted(AB)[1]]
print(rangeAandB([12,3,4,5,6,32,12],[1,5]))
