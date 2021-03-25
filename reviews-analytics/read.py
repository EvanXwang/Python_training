
data = []
count = 0
with open ("reviews.txt", "r") as f: #讀取reviews.txt 並當作變數f  
	for line in f:
		data.append(line)#將每筆line資料加入 data 清單裡
		count += 1
		if count % 1000 == 0: # %是用來求餘數，等於1000筆才印一次 
			print (len(data))

print ("檔案讀取完畢，總共有", len(data), '筆資料') # 算出資料共幾筆



#算出 留言平均長度
sun_len = 0
for d in data:    # 一筆筆讀取長度
	sun_len += len(d)   # 把每一筆資料 加總長度
print ('平均長度是', sun_len / len(data))  


# 篩選概念
new = [] # 建立一個空清單叫 new
for d in data:   #讀取一百萬筆資料
	if len(d) < 100 : # 如果 長度小於100 
		new.append(d) # 則新增進去  new清單
print ('一共有', len(new),'筆留言長度小於100')
print (new[0])


good = []
for d in data :
	if "good" in d :
		good.append(d)
print ('一共有', len(good),'筆留言提到good')
print (good[0])
