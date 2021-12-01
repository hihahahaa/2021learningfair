print('스뭉 분식집 입니다!')

print('''
메뉴판
1. 떡볶이 3000
2. 모듬튀김 3000
3. 돈까스 5000
4.라면 4000
''')
menu = {'떡볶이': 3000, '모듬튀김':3000, '돈까스': 5000, '라면':4000}
foods = {'떡볶이' : '순대 3500원','모듬튀김' : '맥주 3000원','돈까스' : '김밥 2000원','라면' : '김치 1000원'}
hey = {'순대 3500원' : 3500,'맥주 3000원' : 3000,'김밥 2000원' :2000 , '김치 1000원' :1000 }

price = 0
answer = '예'

while answer == "예":
    order = input('메뉴를 선택해주세요:')
    price = price + menu[order]
    print('<%s>궁합음식은 <%s>입니다. 추가 주문하시겠습니까?' % (order, foods[order]))
    a= input('추가 주문하시겠으면 yes 아니면 no 라고 답해주세요')
    if a=='yes':
        price=price+ hey[foods[order]]
    
    answer = input('주문을 더 하시겠습니까? 예,아니오로 답해주세요')
print()
print('결제 금액은', price, '원 입니다.')
print()
print('저희 가게 숫자 맞추기게임에서 성공하시면 50% 할인 쿠폰을 드려요!한번 참여해보세요')
import random
secret_num= random.randint(1,30)

for chance in range(5,0,-1): 
    guess= int(input('1~30 의 숫자중 비밀숫자를 맞춰보세요:'+ '%d번 기회가 남았습니다.' % chance))
    if secret_num == guess:
      print('정답입니다! 50% 할인을 받으실 수 있어요!')
      break
    else:
     if secret_num> guess:
         print('정답보다 작아요!')

         
     else:
         print('정답보다 커요!')


else:
    print('아쉽게도 실패입니다!')
    print('정답은:'+str(secret_num)+'였습니다!')

print()
print('음식이 마음에 드셨다면 5점 만점의 별점을 남겨주세요.')
print('별점 5점 주신분께는 특별히 저희 가게 로또를 드려요! 번호를 맞추시면 사은품도 드려요~')
star = input()
star = int(star)
print('*' * star, '감사합니다')
print()
if star==5:
    

    print('1~45까지의 로또 번호를 입력하고 당첨 결과를 확인해보세요~')

    import random

    list_number=[]


    for i in range(6):
        match= random.randint(1,45)
        while match in list_number:
          match= random.randint(1,45)
        list_number.append(match)
    print()
    list_mynum=[]
    count=1
    while count < 7:
       guess=int(input('%d번째 숫자 입력:'%count))

       if count ==1:
          list_mynum.append(guess)
          count+=1
       else:
          if guess in list_mynum:
            print('이미 존재하는 숫자입니다.')
          else:
            list_mynum.append(guess)
            count+=1
            

    print('입력하신 로또번호==>',end='')
    print(list_mynum)
    print('추첨된  로또번호==>',end='')
    print(list_number)


    if list_number==list_mynum:
       print('당첨되었습니다!!')
    else :
       print('아쉽게도 당첨되지 못하였습니다..')

print()
print('저희 가게를 이용해주셔서 감사합니다~^^')
