import yfinance as yf

SPY=yf.Ticker('SPY')

# get historical market data
spy_2023_hist_1hr= SPY.history(period="1mo", interval="1h", start="2023-01-03", end="2023-11-11")
#print(spy_2023_hist_1hr)

spy_830=[]
spy_930=[]
spy_1030=[]
spy_1130=[]
spy_1230=[]
spy_1330=[]
spy_1430=[]


opening=spy_2023_hist_1hr['Open']
##print(opening)
for i in range(len(opening)):
    if i%7==0:
        spy_830.append(opening[i])
    if i%7==1:
        spy_930.append(opening[i])
    if i%7==2:
        spy_1030.append(opening[i])
    if i%7==3:
        spy_1130.append(opening[i])
    if i%7==4:
        spy_1230.append(opening[i])
    if i%7==5:
        spy_1330.append(opening[i])
    if i%7==6:
        spy_1430.append(opening[i])
        

#print('8:30 times ',spy_830[3])
#print('9:30 times ', spy_930[3])
#print('10:30 times ', spy_1030[3])
#print('11:30 times ', spy_1130[3])
#print('12:30 times ', spy_1230[3])
#print('1:30 times ', spy_1330[3])
#print('2:30 times ', spy_1430[3])
#print('830: ', spy_830[0])
#print('930: ', spy_930[0])

spy830_930_difference=[]
spytotal = []
total = 0
indexnumber=[]
trades=[]
for i in range(len(spy_830)):
    diff = spy_930[i]-spy_830[i]
    spy830_930_difference.append(diff)

for i in range(len(spy830_930_difference)):
    spytotal.append(i)
    if spy830_930_difference[i] <= -1:
        total = total + 1
        indexnumber.append(i)
        trades.append(spy830_930_difference[i])

#print('difference: ', spy830_930_difference[0])
print('length of list: ', len(spy830_930_difference))     
print('total trades: ',len(trades))

ntotal=0
winsprofit = 0
loses = 0
tally=[]
losestreak=0
winstreak = 0
highest=0
temp = 0
for i in indexnumber:
    try:

        diff=(spy_1030[i+2]-spy_930[i])
        if diff >= 1:
            ntotal+=1
            winsprofit=winsprofit+diff*100
            tally.append('2') 
        else:
            tally.append('1')
            loses = loses + 150
    except:
        print('out of range')
for i in tally:
    if i =='1':
        temp+=1
        if temp >= losestreak:
            losestreak = temp 
    elif i =='2':
        temp = 0

for i in tally:
    if i =='2':
        temp+=1
        if temp >= winstreak:
            winstreak = temp 
    elif i =='1':
        temp = 0       


print('wins: ', ntotal)
print('winings $',winsprofit)
print('loses $',loses)
print(f'biggest losing streak = {losestreak}')
print(f'biggest wining streak = {winstreak}')
print('profits if bought last year with strat $',winsprofit-loses)