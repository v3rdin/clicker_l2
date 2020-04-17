#Дебильный бот точильщик v1.0.2

from time import sleep
import pyautogui

#button6fail = pyautogui.locateOnScreen('fail.bmp', grayscale=True, confidence=0.8)
button1svitok = pyautogui.locateOnScreen('svitok.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9)
button2item = pyautogui.locateOnScreen('item.bmp',region=(1507, 295, 400, 350), grayscale=True, confidence=0.9)
#button3kuda = pyautogui.locateOnScreen('kuda.bmp', grayscale=True, confidence=0.9)
#button4start = pyautogui.locateOnScreen('start.bmp', grayscale=True, confidence=0.9)
#button5next = pyautogui.locateOnScreen('next.bmp', grayscale=True, confidence=0.9)
#button6fail = pyautogui.locateOnScreen('fail.bmp', grayscale=True, confidence=0.8)
#button7won = pyautogui.locateOnScreen('won.bmp', grayscale=True, confidence=0.9)
window1 = pyautogui.locateOnScreen('okno.bmp', grayscale=True, confidence=0.9)

print('Ищем окно заточки')
print(window1)
while button1svitok != None:
    if window1 == None:
        window1 = pyautogui.locateOnScreen('okno.bmp', grayscale=True, confidence=0.9) #ищем окно заточки
        button1svitok = pyautogui.locateOnScreen('svitok.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9) #Ищем свиток заточки
        print('Окно заточки не открыто, открываю')
        pyautogui.moveTo(button1svitok, duration=0.2) #идем к свитку
        sleep(0.1)
        pyautogui.doubleClick() #открываем свиток
        sleep(2)
        if window1 != None:
            continue
    if window1 != None:
        print('Окно заточки найдено')
        pyautogui.moveTo(1080, 400) #Убираем курсор
        sleep(0.1)
        button2item = pyautogui.locateOnScreen('item.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9) #Ищем итем
        print(button2item)
        pyautogui.moveTo(button2item)
        if button2item != None:
            print('Тащу шмотку')
            button3kuda = pyautogui.locateOnScreen('kuda.bmp', region=(1754, 808, 71, 70), grayscale=True, confidence=0.9) #Ищем куда тащить
            print(button3kuda)       
            if button3kuda != None:
                #pyautogui.mouseDown()
                print('Куда тащим')
                pyautogui.dragTo(button3kuda, button='left', duration=0.2) #Тащим к слоту заточки
                sleep(0.1)
                #pyautogui.mouseUp()
                button4start = pyautogui.locateOnScreen('start.bmp', region=(1641, 1001, 82, 31), grayscale=True, confidence=0.9) #Ищем кнопку начать
                pyautogui.moveTo(button4start, duration=0.1) #Идем к кнопке "Начать"
                pyautogui.mouseDown()       #Кликаем начать
                sleep(0.1)                  #Кликаем начать
                pyautogui.mouseUp()         #Кликаем начать
                pyautogui.moveTo(1080, 400) #Убираем в сторону курсор, что бы не перекрыть кнопку
                sleep(2)

            button5next = pyautogui.locateOnScreen('next.bmp', region=(1641, 1001, 82, 31), grayscale=True, confidence=0.9)
            print(button5next)
        while button5next != None:
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
            button1svitok = pyautogui.locateOnScreen('svitok.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9)
            button2item = pyautogui.locateOnScreen('item.bmp',region=(1507, 295, 400, 350), grayscale=True, confidence=0.9)
            if button6fail != None or button1svitok == None or button2item == None:
                if button6fail != None:
                    print('Сломалось!')
                pyautogui.press('esc')
                button1svitok = pyautogui.locateOnScreen('svitok.bmp',region=(1500, 290, 400, 350), grayscale=True, confidence=0.9) #Ищем свиток заточки
                pyautogui.moveTo(button1svitok, duration=0.2)
                pyautogui.mouseDown(button='right')
                pyautogui.mouseUp(button='right')
                if button1svitok == None or button2item == None:
                    print('Не нашел свитка или шмотки')
            break