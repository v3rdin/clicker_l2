#Дебильный бот точильщик v1.0.2

from time import sleep
import pyautogui, cv2

confirm1 = pyautogui.confirm('Начинаем точить?','Clicker v1')
if confirm1 == 'OK':
    #button6fail = pyautogui.locateOnScreen('fail.bmp', grayscale=True, confidence=0.8)
    button1svitok = pyautogui.locateOnScreen('item.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9)
    button2item = pyautogui.locateOnScreen('item.bmp',region=(1507, 295, 400, 350), grayscale=True, confidence=0.9)
    #button3kuda = pyautogui.locateOnScreen('kuda.bmp', grayscale=True, confidence=0.9)
    #button4start = pyautogui.locateOnScreen('start.bmp', grayscale=True, confidence=0.9)
    #button5next = pyautogui.locateOnScreen('next.bmp', grayscale=True, confidence=0.9)
    #button6fail = pyautogui.locateOnScreen('fail.bmp', grayscale=True, confidence=0.8)
    #button7won = pyautogui.locateOnScreen('won.bmp', grayscale=True, confidence=0.9)
    #button8accept = pyatogui.locateOnScreen('accept.bmp', grayscale=True, confidence=0.9)
    #button9warning = pyautogui.locateOnScreen('warning.bmp', grayscale=True, confidence=0.9)
    window1 = pyautogui.locateOnScreen('okno.bmp', grayscale=True, confidence=0.9)

    print('Ищем окно заточки')
    print(window1)
    while button1svitok != None:
        if window1 == None:
            print('Окно заточки не открыто, открываю')
            window1 = pyautogui.locateOnScreen('okno.bmp', grayscale=True, confidence=0.9) #ищем окно заточки
            button1svitok = pyautogui.locateOnScreen('item.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9) #Ищем свиток заточки
            pyautogui.moveTo(button1svitok, duration=0.2) #идем к свитку
            sleep(0.1)
            pyautogui.doubleClick() #открываем свиток
            sleep(2)
            if window1 != None:
                continue
        else:
            print('Окно заточки найдено')
            pyautogui.moveTo(1080, 400) #Убираем курсор
            sleep(0.1)
            button2item = pyautogui.locateOnScreen('item.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9) #Ищем итем
            print(button2item)
            pyautogui.moveTo(button2item)
            if button2item != None:
                print('Нашел шмотку')
                button3kuda = pyautogui.locateOnScreen('kuda.bmp', region=(1754, 808, 71, 70), grayscale=True, confidence=0.9) #Ищем куда тащить
                #print(button3kuda)      
                if button3kuda != None:
                    #pyautogui.mouseDown()
                    print('Нашел куда тащить, тащу')
                    pyautogui.dragTo(button3kuda, button='left', duration=0.2) #Тащим к слоту заточки
                    sleep(0.1)
                    #pyautogui.mouseUp()
                    button4start = pyautogui.locateOnScreen('start.bmp', region=(1641, 1001, 82, 31), grayscale=True, confidence=0.9) #Ищем кнопку начать
                    if button4start != None:
                        print('Вижу кнопку "Начать"')
                        pyautogui.moveTo(button4start, duration=0.1) #Идем к кнопке "Начать"
                        pyautogui.mouseDown()       #Кликаем начать
                        sleep(0.1)                  #Кликаем начать
                        pyautogui.mouseUp()         #Кликаем начать
                        pyautogui.moveTo(1080, 400) #Убираем в сторону курсор, что бы не перекрыть кнопку
                        button9warning = pyautogui.locateOnScreen('warning.bmp', grayscale=True, confidence=0.9)
                        if button9warning != None:
                            print('Вижу предупреждение')
                            button8accept = pyautogui.locateOnScreen('accept.bmp', grayscale=True, confidence=0.9)
                            pyautogui.moveTo(button8accept, duration=0.1)
                            pyautogui.mouseDown()       #Кликаем подтвердить
                            sleep(0.1)                  #Кликаем подтвердить
                            pyautogui.mouseUp()         #Кликаем подтвердить
                            sleep(2.5)
                        else:
                            sleep(2.5)
                    else:
                        print('Не вижу кнопку "Начать", иду дальше')
                else:
                    print('Не нашел куда тащить !')
            else:
                print('Не нашел шмотку!')
                break
            button5next = pyautogui.locateOnScreen('next.bmp', region=(1641, 1001, 82, 31), grayscale=True, confidence=0.9)
            print(button5next)
            while button5next != None:
                button9warning = pyautogui.locateOnScreen('warning.bmp', grayscale=True, confidence=0.9)
                if button9warning != None:
                    print('Вижу предупреждение')
                    button8accept = pyautogui.locateOnScreen('accept.bmp', grayscale=True, confidence=0.9)
                    pyautogui.moveTo(button8accept, duration=0.1)
                    pyautogui.mouseDown()       #Кликаем подтвердить
                    sleep(0.1)                  #Кликаем подтвердить
                    pyautogui.mouseUp()         #Кликаем подтвердить
                    sleep(2.5)
                else:
                    button5next = pyautogui.locateOnScreen('next.bmp', region=(1641, 1001, 82, 31), grayscale=True, confidence=0.9)
                    print(button5next)
                    print('Ищу кнопку "Продолжить"')
                    print('Кнопка продолжить')
                    print('Точим дальше')
                    pyautogui.moveTo(button5next, duration=0.1)
                    pyautogui.mouseDown(button='left')
                    pyautogui.mouseUp(button='left')
                    sleep(0.15)
                    pyautogui.mouseDown(button='left')
                    pyautogui.mouseUp(button='left')
                    pyautogui.moveTo(1080, 400) #Убираем в сторону курсор, что бы не перекрыть кнопку
                    sleep(2.5)    
                    button6fail = pyautogui.locateOnScreen('fail.bmp', grayscale=True, confidence=0.9)
                    print(button6fail)
                    print('Ищу сломанное')
                    button1svitok = pyautogui.locateOnScreen('item.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9)
                    button2item = pyautogui.locateOnScreen('item.bmp',region=(1507, 295, 400, 350), grayscale=True, confidence=0.9)
                    if button6fail != None or button1svitok == None or button2item == None:
                        if button6fail != None:
                            print('Сломалось!')
                        button9close = pyautogui.locateOnScreen('close.bmp', grayscale=True, confidence=0.9)
                        pyautogui.moveTo(button9close, duration=0.1)
                        pyautogui.mouseDown(button='left')
                        pyautogui.mouseUp(button='left')
                        button1svitok = pyautogui.locateOnScreen('item.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9) #Ищем свиток заточки
                        pyautogui.moveTo(button1svitok, duration=0.2)
                        pyautogui.mouseDown(button='right')
                        pyautogui.mouseUp(button='right')
                        if button2item == None:
                            button2item = pyautogui.locateOnScreen('item.bmp',region=(1507, 295, 400, 350), grayscale=True, confidence=0.9)
                            if button2item !=None:
                                continue
                            else:
                                print('Не нашел шмотки!')
                        if button1svitok == None:
                            button1svitok = pyautogui.locateOnScreen('item.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9)
                            if button1svitok != None:
                                continue
                            else:
                                print('Не нашел свитка!')
                            break
            else:
                print('Не вижу кнопку "Продолжить"')
                button6fail = pyautogui.locateOnScreen('fail.bmp', grayscale=True, confidence=0.8)
                button1svitok = pyautogui.locateOnScreen('item.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9)
                button2item = pyautogui.locateOnScreen('item.bmp',region=(1507, 295, 400, 350), grayscale=True, confidence=0.9)
                if button6fail != None or button1svitok == None or button2item == None:
                    if button6fail != None:
                        print('Сломалось!')
                    pyautogui.press('esc')
                    button1svitok = pyautogui.locateOnScreen('item.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9) #Ищем свиток заточки
                    pyautogui.moveTo(button1svitok, duration=0.2)
                    pyautogui.mouseDown(button='right')
                    pyautogui.mouseUp(button='right')
                    if button2item == None: 
                        print('Не нашел шмотки!')
                    if button1svitok == None:
                        print('Не нашел свитка!')
                        break
    else:
        print('Не нашел свитка!!!')
else:
    exit()