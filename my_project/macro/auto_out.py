def auto_out():
    # λͺ¨λ λ°? ?¨?€μ§?
    import pyautogui # λ§μ°?€ μ‘°μ?© 
    from datetime import datetime # ??¬?κ°? μΆλ ₯?©
    import urllib.request # ?λ²μκ°? κ°?? Έ?€κΈ?
    import time # ?? ?΄?©
    import os # μ»΄ν¨?° ?κΈ? ?©

    #??¬ ?κ°? μΆλ ₯ λ°? ?΄λ¦?
    while True:    
        # ?λ²μκ°? μΆλ ₯ 
        month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
            'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        
        url = 'https://edu.ssafy.com'
        date = urllib.request.urlopen(url).headers['Date'][5:-4]
        d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], int(date[12:14]) + 9 , date[15:17], date[18:]
        min_str = str(min)
        hour_str = str(hour)
    
        print(f'[{url}]? ?λ²μκ°?\n{y}? {m}? {d}?Ό {hour}? {min}λΆ? {sec}μ΄?')
        time.sleep(2) # ?? ?΄ 3μ΄? 

        if hour_str == '18' and min_str == '00': # λ§μ½ 18?κ°? ?λ©? 
            
            #?΄λ¦? #Point(x=653, y=343)
            pyautogui.click(651,341,button='left',clicks =2, interval =1) #?΄?€ ?΄λ¦? 
    
            #?΄λ¦? λ©μΈμ§? μΆλ ₯
            print("?΄λ¦? ??΅??€.")
            time.sleep(2) 
            break
    #μ»΄ν¨?° ?κΈ?
    os.system('shutdown -l') # λ‘κ·Έ??
    os.system('shutdown -s -t 5') # 10μ΄? ?€ μ»΄ν¨?° μ’λ£



if __name__ == '__main__':
    auto_out()