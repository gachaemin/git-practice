age=int(input('나이를 입력하세요:'))
balance=5000
if age>=8 and age<=12:
    balance-=650
elif age>=13 and age<=18:
    balance-=1050
elif age>=19 and age<=59:
    balance-=1250
print('잔액=',balance)

