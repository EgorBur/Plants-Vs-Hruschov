import pygame
import sys
import time
import random

WHITE = (255, 255, 255)
CREM = (180, 170, 120)
BLACK = (0, 0, 0)
BROWN = (100, 50, 30)
YELLOW = (225, 225, 0)
RED = (252, 42, 42)
GREEN = (2, 206, 19)
BLUE = (0, 162, 255)

#sc = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#ox, oy = sc.get_size()
#Oh = oy - 250
#cl = Oh // 5

cl = 160 #160
sc = pygame.display.set_mode((cl * 9, cl * 5 + cl))

a = 0
b = 0
x = 0
y = 0
flag = 0
flagB = 0
flagC = 0
flagSV = 0
flagAT = 0
flagSHB = 0
flagSHC = 0
flagH = 0
flagM = 0
flagMM = False
flagZ = 0
game = 1
x0 = 0
y0 = 80
hx = 0
hy = 0
n = 0
p = 0
kol = 17
g = 555
pod = 0
gor = 0
zom = 0
strr = 0
minn = 0
lasttime = 0
flagSTR = 0

Xg = []
Yg = []
Xp = []
Yp = []
Xm = []
Ym = []
Xz = []
Yz = []
Xs = []
Ys = []
XpP = []
XpZ = []

Lt = []

Xsh = [0, cl*1, cl*2, cl*3, cl*4, cl*5, cl*6, cl*7, cl*8]
Ysh = [cl*5, cl*5, cl*5, cl*5, cl*5, cl*5, cl*5, cl*5, cl*5]

def pole():
    global cl
    global a
    global b
    global x
    global y
    flag = 0

 
    pygame.draw.rect(sc, GREEN, (0, 0, cl * 9, cl * 5))
    pygame.draw.rect(sc, YELLOW, (0, cl * 5, cl * 9, cl * 1))


    a = 0
    b = 0
    y = 0
    x = 0

    if flag == 0:
        while a < 9:
            pygame.draw.line(sc, RED, [x, 0], [x, cl * 6], 1) ## vert
            a += 1
            x += cl
        a = 0
        while a < 6:
            pygame.draw.line(sc, RED, [0, y], [cl * 9, y], 1) ## goriz
            a += 1
            y += cl
        flag = 1
    a = 0
    b = 0
    y = 0
    x = 0

img0 = pygame.image.load("Plants Vs Hruschov\goroh.png").convert_alpha()
img1 =pygame.transform.scale(img0, (cl, cl))
def goroh(x, y): 
    sc.blit(img1, (x, y))

img01 = pygame.image.load("Plants Vs Hruschov\pods.png").convert_alpha()
img2 =pygame.transform.scale(img01, (cl, cl))
def pods(x, y): 
    sc.blit(img2, (x, y))

img03 = pygame.image.load("Plants Vs Hruschov\mina.png").convert_alpha()
img4 =pygame.transform.scale(img03, (cl - 25, cl - 5))
def mina(x, y):
    sc.blit(img4, (x + 12, y + 2))

img02 = pygame.image.load("Plants Vs Hruschov\hrusch.png").convert_alpha()
img3 =pygame.transform.scale(img02, (cl-10, cl-10))
def hrusch(x, y):
    sc.blit(img3, (x + 5, y + 5))

def snar(x, y):
    pygame.draw.circle(sc, RED, (x + cl*1.14, y + cl*0.25), cl/8)

def stat(x, y):
    itg = 0
    c = 0
    f = 0
    l = 0
    u = 0
    while c < pod:
        if x == Xp[c] and y == Yp[c]:
            itg = 1 # ZANYATO
            return itg
        else:
            itg = 0 # SVOBODNO
        c += 1
    
    while l < gor:
        if x == Xg[l] and y == Yg[l]:
            itg = 1 # ZANYATO
            return itg
        else:
            itg = 0 # SVOBODNO
        l += 1
    
    while u < minn:
        if x == Xm[u] and y == Ym[u]:
            itg = 1 # ZANYATO
            return itg
        else:
            itg = 0 # SVOBODNO
        u += 1

    while f < zom:
        if x == Xz[f] and y == Yz[f]:
            itg = 1 # ZANYATO
            return itg
        else:
            itg = 0 # SVOBODNO
        f += 1
    return itg

def shop():
    d = 0
    global p
    while d < 9:
        if mX > Xsh[d] and mX < Xsh[d] + cl and mY > Ysh[d] and mY < Ysh[d] + cl and flagMM == 1:
            print(d)
            p = d
            break
        else:
            d += 1
    return p

def zomb():
    global Xz
    global Yz
    global XpZ
    global zom
    X = 8
    Y = random.randint(0, 4)
    hrusch(X * cl, Y * cl)
    Xz += [X * cl]
    Yz += [Y * cl]
    XpZ += [5]
    zom += 1

def shag():
    t = 0
    while t < zom:
        Xz[t] -= cl
        #print(Xz[t])
        #print("ZZZZZZZZ")
        t += 1

def rast():
    imgs1 =pygame.transform.scale(img01, (cl-10, cl-10))
    sc.blit(imgs1, (5, 805))
    imgs2 =pygame.transform.scale(img0, (cl-10, cl-10))
    sc.blit(imgs2, (165, 805))
    imgs3 =pygame.transform.scale(img03, (cl-10, cl-10))
    sc.blit(imgs3, (325, 805))
    w = 0
    while w < gor:
        goroh(Xg[w], Yg[w])
        w += 1

    w = 0
    while w < strr:
        snar(Xs[w], Ys[w])
        w += 1

    w = 0
    while w < pod:
        pods(Xp[w], Yp[w])
        w += 1
    
    w = 0
    while w < minn:
        mina(Xm[w], Ym[w])
        w += 1

    w = 0
    while w < zom:
        if Xz[w] >= 0:
            hrusch(Xz[w], Yz[w])
            w += 1
        else:
            w += 1


pole()
rast()
lasttime = time.time()

while game == 1:#######################################################################
    mB, mm, mmm = pygame.mouse.get_pressed(num_buttons=3)
    mX, mY = pygame.mouse.get_pos()
    mkx = mX//cl * cl
    mky = mY//cl * cl

    if mB == 1 and flagM == 0:
        flagMM = 1
        flagM = 1
    else:
        flagMM = 0
    if mB == 0 and flagM == 1:
        flagM = 0


    #####################
    pole()
    rast()

    i = 0
    while i < strr:
        q = 0
        while q < zom:
            #print("\n", "I:", i)
            #print(Xs)
            if len(Xs) > 1:
                if Xs[i] >= Xz[q] - cl and Xs[i] < Xz[q] and Ys[i] == Yz[q]:
                    print("q:", q)
                    XpZ[q] -= 1
                    print(Yz[q], XpZ[q])
                    if XpZ[q] <= 0:
                        Xz.pop(q)
                        Yz.pop(q)
                        XpZ.pop(q)
                        zom -= 1
                    Xs.pop(i)
                    Ys.pop(i)
                    strr -= 1
                    #print("AAAAAAAAAAAAAAAAAAAAAAAAA")
                    #print("I2:", i)
                    if i > 1:
                        i -= 1
            q += 1
        i += 1

    ## цикл ласттаймов
    v = 0
    while v < gor:
        if time.time() - Lt[v] > 3:
            w = 0
            while w < zom:
                if Yg[v] == Yz[w]:
                    Xs += [Xg[v]]
                    Ys += [Yg[v]]
                    strr += 1
                    flagSTR = 1
                    Lt[v] = time.time()
                    asd = time.time()
                elif Yg[v] != Yz[w]:
                    #print("pizda11111")
                    Lt[v] = time.time()
                w += 1
        v += 1
    ## цикл ласттаймов

    if flagSTR == 1:
        v = 0
        if time.time() - asd > 0.01:
            while v < strr:
                Xs[v] += 10
                asd = time.time()
                v += 1
    
    ##########      ##########     ##########     ##########     TIME
    if time.time() - lasttime > 2.5:
        shag()
        zomb()
        lasttime = time.time()
    ##########      ##########     ##########     ##########     TIME

    if mY > cl*5:
        g = shop()

    if mY < cl*5:
        if g == 0:
            sv = stat(mkx, mky)
            if sv == 1:
                #print("zanyato blyaaaaaa")
                pass
            if sv == 0 and mB == 1:
                Xp += [mkx]
                Yp += [mky] 
                pod += 1
                g = 555

        if g == 1:
            sv = stat(mkx, mky)
            if sv == 1:
                #print("zanyato")
                pass
            if sv == 0 and mB == 1:
                Xg += [mkx]
                Yg += [mky]
                Lt += [time.time()]
                gor += 1
                g = 555
        
        if g == 2:
            sv = stat(mkx, mky)
            if sv == 1:
                #print("zanyato blyaaaaaa")
                pass
            if sv == 0 and mB == 1:
                mina(mkx, mky)
                Xm += [mkx]
                Ym += [mky]
                minn += 1
                g = 555

        if g == 8:
            sv = stat(mkx, mky)
            if sv == 1:
                pass
            if sv == 0 and mB == 1:
                Xz += [mkx]
                Yz += [mky]
                XpZ += [5]
                zom += 1
                g = 555

    
    ##sc.blit(img, (0, 0))





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print(Xp)
            print(Yp)
            print(Xg)
            print(Yg)
            print(Xs)
            print(Ys)
            print(Lt)
            sys.exit()
    pygame.display.update()

while game == 0:
    print("Конец игры")
    pygame.quit()
    sys.exit()
