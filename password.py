password = 'a123456'   # 創造第一個物件: 答案
i = 3 # ,剩餘機會 ,  創造第二個物件  
while True:
    pwd = input('請輸入密碼: ')    # 使用者輸入的東西 , 方便不用兩次改
    if pwd == password:             #登入者輸入的pwd = 預設好的password 
        print('登入成功!')  
        break # 逃出迴圈 , 一登入就要break 
    else: 
        i = i -1 
        print( '密碼錯誤! 還有' , i , '次機會')
        if i == 0:
            break  #  0次機會就會break 
