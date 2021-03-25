import os ,sys
os.system('clear')

def menu():        #功能選單
    fun = input('\t(0) 離開程式\n\t(1) 列出檔案\n\t(2) 列出資料夾\
    \n\t(3) 顯示檔案內容\n\t(4) 刪除檔案內容\n\t(5) 執行檔案\
    \n\t(6) 進入資料夾\n\t(7) 刪除資料夾\n\t(8) 回上層資料夾\
    \n操作:')
    return fun
def list ():       #列出路徑清單索引
    list = [item for item in os.listdir()]
    for i in range(0,len(os.listdir())):
        print (i,' ',list[i])
def list_dir ():   #列出資料夾
    print (os.getcwd())
def read_dir ():       #讀取檔案路徑
    while True:
        list = os.listdir()
        a = int(input('輸入檔案索引'))  #輸入該檔案索引
        b = os.getcwd()            #讀取檔案路徑
        c = b+'/'+list[a]          #合併路徑
        return c        

def read_file (a):     #讀取檔案內容
    with open(a,'r') as f:
        print(f.read())
def remove_file(a):    #刪除檔案

    os.remove(a)
def remove_dir(a):     #刪除資料夾
    os.rmdir(a)
    
class File ():         # 主程式
    while True:
        print ('工作路徑:',os.getcwd())
        fun = menu()
        os.system('clear')

        if fun == '0':
            break

        elif fun == '1':
            list()
            print ('\n')

        elif fun == '2':
            list_dir()

        elif fun == '3':
            try:
                list()
                a = read_dir()
                read_file(a)
            except :
                pass

        elif fun == '4':
            try:
                list()
                a = read_dir()
                remove_file(a)
            except :
                pass

        elif fun == '5':
            list()
            file_os = input ('請輸入command')
            os.system(file_os)

        elif fun == '6':
            try:
                list()
                a = read_dir ()
                os.chdir(a)
            except :
                pass

        elif fun == '7':
            try:
                list()
                a = read_dir()
                remove_dir(a)
            except :
                pass

        elif fun == '8':
            os.chdir("..")  

File()





