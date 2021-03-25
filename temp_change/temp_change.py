temp = input ('請輸入攝氏溫度：')

def funtion (temp):
    answer = float(temp) * 5 / 9 + 32
    print('華氏溫度為 ', round(answer, 2)) # round 取小數點第二位


funtion(temp)