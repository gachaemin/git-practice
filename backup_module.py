# 할인 쿠폰 시스템 만들기

price = int(input('가격을 입력하세요: '))
coupon = input('쿠폰을 입력하세요(vip/member/etc): ')

if coupon=='vip':
    total=price - (price * 0.3)

elif coupon =='member':
    total=price-(price * 0.2)

else:
    total=price-(price * 0.05)

print('할인된 가격은 ' ,format(int(total)))
