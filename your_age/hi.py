name = input('請輸入名字:')
age = input ("請輸入你的年紀")
if int(age) < 18:
    print('hello', name,'你未滿18歲，不得飲酒')
else :
    print('hello', name,'飲酒不得過量')