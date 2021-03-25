# 產生一個隨機整數 1~100 （不要印出來）
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 “終於猜對了”
# 猜錯的話 要告訴他 比答案大/小
# 印出猜了幾次
# 讓使用者決定隨機數範圍

start = input ("隨機數起始值：") # 變數名稱不要亂取，盡量取意思相近詞
end = input ("隨機數結束值：")  
start = int(start)  # 型態轉換成 整數
end = int(end)
import random
r =  random.randint(start,end)
count = 0  # 計算猜的次數 ，需要在while迴圈外，否則會一直歸零
while True :
	num = input ("請猜數字  ： ")
	num = int(num)
	count += 1   # 意思就是 count = count + 1  
	if num == r :
		print ("終於猜對了")
		print ("你猜了", count,"次")
		break
	elif num > r :
		print ("比答案大")

	elif num < r :
		print ("比答案小")

	print ("你猜了", count,"次")  # 寫elif外圈 ，避免重覆寫二次

