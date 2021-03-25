import random
win = 0
lose = 0
for times in range(100000):
    # 準備三門
    doors = ['羊','羊']
    car = random.randint(0,2)
    doors.insert(car,'車')
    print (doors)

    # 讓參賽者挑一個門
    car = random.randint(0,2)
    print ('使用者選的:',doors[car])
    del doors[car]
    print ('剩下門:',doors)

    # 主持人開一隻羊出來
    doors.remove('羊')
    print('最後剩下的門:',doors)

    # 確定一下到底是輸還是贏
    if doors[0] == '車':
        print ('羸了')
        win += 1
    else:
        print ('輸了')
        lose += 1

total = win + lose
print ('贏的次數:', win)
print ('輸的次數:', lose)
print('贏的機率:', win / total * 100 ,'%' )
print('輸的機率:', lose / total * 100 ,'%' )





