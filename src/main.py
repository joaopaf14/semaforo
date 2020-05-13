from led import Led
from button import Button
from utime import sleep, ticks_ms, ticks_add
lr = Led(21)
ly = Led(22)
lg = Led(19)

def peao(state):
    global nl
    if nl == 1 or nl==0:
        nl=4

def inte(state):
    if state ==True:
        global nl, last
        if nl == 5:
            last = time
            nl=0
        else:
            last = time
            nl=5
bp = Button(23,peao)
bi = Button(18, inte)


last = ticks_ms()
time = 0
l = 0
while True:
    # print(l)
    time = ticks_ms()
    # print(time,last)
    if l==0:
        lg.on()
        lr.off()
        ly.off()
        nl=1
    if l==1:
        if time - last > 9000:
            last = time
            lg.off()
            ly.on()
            nl = 2
    if l==2:
        if time - last > 1000:
            last = time
            ly.off()
            lr.on()
            nl=3
    if l ==3:
        if time - last  > 5000:
            last = time
            lr.off()
            lg.on()
            nl =1
    if l==4:
        if time - last > 4000:
            last = time
            lg.off()
            ly.on()
            nl = 2
    if l==5:
        lg.off()
        lr.off()
        if time - last < 1000:
            ly.on()
        if time - last >1000 and time - last < 2000:
            ly.off()
        if time - last>2000:
            last = time
            
            
        
    bi.proc()
    bp.proc()
    # print(time-last)
    l = nl

