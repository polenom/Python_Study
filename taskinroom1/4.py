basa = {'Беларусь': {'Минск': 2009786, 'Брест' :354318, 'Гомель' : 507795}, 'Польша': {'Варшава' :1793579 , 'Вроцлав' : 641607 }, 'Литва':{ 'Вильнюс' : 588412}}
N,N1 =input().split()
print(basa[N][N1]basa = {'Беларусь': {'Минск': 2009786, 'Брест' :354318, 'Гомель' : 507795}, 'Польша': {'Варшава' :1793579 , 'Вроцлав' : 641607 }, 'Литва':{ 'Вильнюс' : 588412}}
N,N1 =input().split()
if basa.get(N, None) == None:
    print('В базе нет страны')
elif basa[N].get(N1, None) == None:
    print('В базе нет города')    
else:
    print(basa.get(N, dict()).get(N1)))
