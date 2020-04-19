#Быдло бот точильщик v1.0.2
#Точит благой точкой, не запрашивается подтверждение

from time import sleep
import pyautogui, cv2

def button1svitok():
    return pyautogui.locateOnScreen('svitok.bmp',region=(1480, 295, 440, 420), grayscale=True, confidence=0.9)
def button2item():
    return pyautogui.locateOnScreen('item.bmp',region=(1480, 295, 440, 420), grayscale=True, confidence=0.9)
def button3kuda():
    return pyautogui.locateOnScreen('kuda.bmp',region=(1570, 760, 630, 165), grayscale=True, confidence=0.9)
def button4start():
    return pyautogui.locateOnScreen('start.bmp',region=(1650, 1000, 170, 45), grayscale=True, confidence=0.9)
def button5next():
    return pyautogui.locateOnScreen('next.bmp',region=(1650, 1000, 90, 40), grayscale=True, confidence=0.9)
def button6fail():
    return pyautogui.locateOnScreen('fail.bmp',region=(1575, 930, 330, 50), grayscale=True, confidence=0.8)
def button7won():
    return pyautogui.locateOnScreen('won.bmp',region=(1575, 930, 330, 50), grayscale=True, confidence=0.9)
def button8accept():
    return pyautogui.locateOnScreen('accept.bmp', grayscale=True, confidence=0.9)
def button9warning():
    return pyautogui.locateOnScreen('warning.bmp', grayscale=True, confidence=0.9)
def button10close():
    return pyautogui.locateOnScreen('close.bmp',region=(1650, 1000, 170, 45), grayscale=True, confidence=0.9)
def window1():
    return pyautogui.locateOnScreen('okno.bmp', grayscale=True, confidence=0.9)

confirm1 = pyautogui.confirm('Начинаем точить?','Clicker v1')
if confirm1 == 'OK':
    print('Ищем окно заточки')
    print(window1())
    button1svitok()
    while button1svitok() != None:
        if window1() == None:
            print('Окно заточки не открыто, открываю')
            window1() #ищем окно заточки
            pyautogui.moveTo(button1svitok(), duration=0.2) #идем к свитку
            sleep(0.1)
            pyautogui.doubleClick() #открываем свиток
            sleep(2)
            if window1() != None:
                continue
        else:
            print('Окно заточки найдено')
            pyautogui.moveTo(1080, 400) #Убираем курсор
            sleep(0.1)
            pyautogui.moveTo(button2item())
            if button2item() != None:
                print('Нашел шмотку')
                button3kuda() #Ищем куда тащить     
                if button3kuda() != None:
                    print('Нашел куда тащить, тащу')
                    pyautogui.dragTo(button3kuda(), button='left', duration=0.2) #Тащим к слоту заточки
                    sleep(0.1)
                    button4start() #Ищем кнопку начать
                    if button4start() != None:
                        print('Вижу кнопку "Начать"')
                        pyautogui.moveTo(button4start(), duration=0.1) #Идем к кнопке "Начать"
                        pyautogui.mouseDown()       #Кликаем начать
                        sleep(0.1)                  #Кликаем начать
                        pyautogui.mouseUp()         #Кликаем начать
                        pyautogui.moveTo(1080, 400) #Убираем в сторону курсор, что бы не перекрыть кнопку
                        button9warning()
                        if button9warning() != None:
                            print('Вижу предупреждение')
                            button8accept()
                            pyautogui.moveTo(button8accept(), duration=0.1)
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
            print(button5next())
            while button5next() != None:
                button5next()
                print('Ищу кнопку "Продолжить"')
                print('Кнопка продолжить')
                print('Точим дальше')
                pyautogui.moveTo(button5next(), duration=0.1)
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                sleep(0.15)
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
                pyautogui.moveTo(1080, 400) #Убираем в сторону курсор, что бы не перекрыть кнопку
                sleep(2.5)    
                print(button6fail())
                print('Ищу сломанное')
                button1svitok()
                button2item()
                if button6fail() != None or button1svitok() == None or button2item() == None:
                    if button6fail() != None:
                        print('Сломалось!')
                    button10close()
                    pyautogui.moveTo(button10close(), duration=0.1)
                    pyautogui.mouseDown(button='left')
                    pyautogui.mouseUp(button='left')
                    button1svitok() #Ищем свиток заточки
                    pyautogui.moveTo(button1svitok(), duration=0.2)
                    pyautogui.mouseDown(button='right')
                    pyautogui.mouseUp(button='right')
                    if button2item() == None:
                        button2item()
                        if button2item() !=None:
                            continue
                        else:
                            print('Не нашел шмотки!')
                    if button1svitok() == None:
                        button1svitok()
                        if button1svitok() != None:
                            continue
                        else:
                            print('Не нашел свитка!')
                        break
            else:
                print('Не вижу кнопку "Продолжить"')
                button6fail()
                button1svitok()
                button2item()
                if button6fail() != None or button1svitok() == None or button2item() == None:
                    if button6fail != None:
                        print('Сломалось!')
                    pyautogui.press('esc')
                    button1svitok() #Ищем свиток заточки
                    pyautogui.moveTo(button1svitok(), duration=0.2)
                    pyautogui.mouseDown(button='right')
                    pyautogui.mouseUp(button='right')
                    if button2item() == None: 
                        print('Не нашел шмотки!')
                    if button1svitok() == None:
                        print('Не нашел свитка!')
                        break
    else:
        print('Не нашел свитка!!!')
else:
    exit()