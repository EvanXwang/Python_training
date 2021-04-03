import random

prize = set()
while len(prize) < 7 :
    n = random.randint(1, 48)
    prize.add(n)
print('頭獎彩券:', prize)
times = 0

while True:
    lottery = set()

    while len(lottery) < 7:
        n = random.randint(1, 48)
        lottery.add(n)
    print('我買的彩券:', lottery)
    times += 1
    total = 0

    for n in lottery:
        if n in prize:
            print('中獎號碼為:', n)
            total += 1

    print('中獎號碼共有:', total)

    if total >= 6:  # 設定中n個號碼，計算買的張數，和機率為何??
        print('總共買了幾張:', times)
        n = (1 / times) * 100
        print('中獎機率為:', n, '%')
        break

