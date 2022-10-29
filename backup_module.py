number=int(input('4자리 정수를 입력하세요:'))
sum=0
a=(number//1000)%10
b=(number//100)%10
c=(number//10)%10
d=number%10
sum=a+b+c+d
print('자리수의 합은' , sum , '이다.')
