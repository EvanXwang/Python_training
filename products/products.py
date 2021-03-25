# while 迴圈適合用在不知會用幾次情況下
products = []
while True :
	name = input ('請輸入商品名稱：')
	if name == 'q':
		break
	price = input ('請輸入價格')
	products.append([name,price]) # 二維清單 （同個位置有多個input)
print (products)

for p in products:
	print (p[0], '的價格是', p[1])


with open ('products.csv' , 'w' , encoding='utf-8') as f : 
        # with 可自動colse檔案 ，'w' 寫入
        # utf-8 中文編碼 ，在MAC好像沒這問題，excel好像需要加入此行
	f.write('商品' + ',' + '價格' + '\n')
	for p in products:
		f.write (p[0]+ ',' + p[1] + '\n') 
		# 逗點是一個表格（在試算表裡）
		# \n 是換行的意思