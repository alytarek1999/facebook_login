import pyautogui as pg
import time as t

u1=" "
p1=" "

def auto(u1,p1):
    t.sleep(1)
    pg.moveTo(x=514, y=767,duration=1)
    brow=pg.locateCenterOnScreen("p8.png",confidence=0.6)
    while brow==None:
        brow=pg.locateCenterOnScreen("p8.png",confidence=0.6)
        t.sleep(1)
    pg.moveTo(brow,duration=1)
    pg.click()
    url=pg.locateCenterOnScreen("p4.png")
    while url==None:
        url=pg.locateCenterOnScreen("p4.png")
        t.sleep(1)
    pg.moveTo(url,duration=1)
    pg.click()
    pg.typewrite("https://www.facebook.com/login.php/")
    pg.hotkey("enter")
    use=pg.locateCenterOnScreen("p2.png")
    while use==None:
        use=pg.locateCenterOnScreen("p2.png")
        t.sleep(1)
    #pg.moveTo(use,duration=1)
    #pg.click()
    pg.typewrite(u1)
    t.sleep(1)
    pg.hotkey("tab")
    pg.typewrite(p1)
    t.sleep(1)
    pg.hotkey("enter")
    prof=pg.locateCenterOnScreen("p3.png")
    while prof==None:
        prof=pg.locateCenterOnScreen("p3.png")
        t.sleep(1)
    pg.moveTo(prof,duration=1)
    pg.click()
    prof2=pg.locateCenterOnScreen("p7.png")
    while prof==None:
        prof2=pg.locateCenterOnScreen("p7.png")
        t.sleep(1)
    like=pg.locateCenterOnScreen("p5.png")
    while like==None:
        pg.scroll(-100)
        like=pg.locateCenterOnScreen("p5.png")
        t.sleep(1)
    pg.moveTo(like,duration=1)
    love=pg.locateCenterOnScreen("p6.png")
    while love==None:
        love=pg.locateCenterOnScreen("p6.png")
    pg.moveTo(love,duration=1)
    pg.click()

