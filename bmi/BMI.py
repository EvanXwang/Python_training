# BMI公式
def bmi(x):
    if x >=18.5 and x < 24:
        print('正常')
    elif x <18.5 :
        print('體重過輕')
    elif x >=24 and x <27:
        print('過重')
    elif x >=27 and x <30:
        print('輕度肥胖')
    elif x >=30 and x <35:
        print('重度肥胖')

#輸入個人資訊並回傳參數
def xxx():

    height = int(input('請輸入身高 '))
    weight = int(input('請輸入體重 '))
    bmi = weight / (height/100)**2
    return bmi

mybmi = xxx()
bmi(mybmi)



