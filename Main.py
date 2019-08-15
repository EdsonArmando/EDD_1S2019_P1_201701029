import sys,os
import curses
import random
import subprocess
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from Structures.CircularDoubleList import Circular_Double_List
from Structures.ScoreStack import Score_Stack
from Structures.ScoreBoardQueue import ScoreBoard_Queue
queue = ScoreBoard_Queue()
cir = Circular_Double_List()

stdscr = curses.initscr()
win = curses.newwin(30,120,0,0)
curses.noecho()
curses.cbreak()
curses.curs_set(0)
win.keypad(True)
key=KEY_LEFT
def playGame(name):
    curses.curs_set(0)
    curses.noecho()
    conta=0
    stack = Score_Stack()
    win.clear()
    win.clear()
    curses.curs_set(0)
    point=0
    x=random.randint(2,120-2)
    y=random.randint(2,30-2)
    x_x=random.randint(2,120-2)
    y_y=random.randint(2,30-2)
    win.border(0)
    key = KEY_RIGHT
    locX = 5
    locY = 5
    foodSneak1(x,y,0)
    win.addstr(0,45, 'User: '+ name)
    win.addch(locY,locX,'#')
    while 1:
        type = random.randint(0,40)
        if point<=15:
            win.timeout((100 - 38//3)%90)
        elif point>15:
            win.timeout((100 - 20//3)%90)
        inputKey = win.getch()
        if inputKey is not  -1:
            key = inputKey
        win.addch(locY,locX,' ')
        if key == KEY_RIGHT:
            conta=0
            win.addch(locY,locX-2,' ')
            if locX==x and locY==y:
                point+=1
                stack.PushScore(x,y)
                x=random.randint(2,120-2)
                y=random.randint(2,30-2)

                if type <=5 :
                    x_x=random.randint(2,120-2)
                    y_y=random.randint(2,30-2)
                    foodSneak2(x_x,y_y,point)
                else:
                    foodSneak1(x,y,point)

            elif locX==x_x and locY==y_y:
                point -=1
                stack.PopScore()
                x_x=random.randint(2,120-2)
                y_y=random.randint(2,30-2)
                if type <=5 :
                    foodSneak2(x_x,y_y,point)
                else:
                    x=random.randint(2,120-2)
                    y=random.randint(2,30-2)
                    foodSneak1(x,y,point)
            locX = locX + 1
        elif key == KEY_LEFT:
            conta=0
            win.addch(locY,locX-2,' ')
            if locX==x and locY==y:
                point+=1
                stack.PushScore(x,y)
                x=random.randint(2,120-2)
                y=random.randint(2,30-2)
                if type <=5 :
                    x_x=random.randint(2,120-2)
                    y_y=random.randint(2,30-2)
                    foodSneak2(x_x,y_y,point)
                else:
                    foodSneak1(x,y,point)

            elif locX==x_x and locY==y_y:
                point -=1
                stack.PopScore()
                x_x=random.randint(2,120-2)
                y_y=random.randint(2,30-2)

                if type <=5 :
                    foodSneak2(x_x,y_y,point)
                else:
                    x=random.randint(2,120-2)
                    y=random.randint(2,30-2)
                    foodSneak1(x,y,point)
            locX = locX - 1
        elif key == KEY_UP:
            conta=0
            win.addch(locY,locX-3,' ')
            win.addch(locY,locX-2,' ')
            win.addch(locY,locX-1,' ')
            if locX==x and locY==y or locX-1==x and locY==y or locX-2==x and locY==y or locX-3==x and locY==y :
                point+=1
                stack.PushScore(x,y)
                x=random.randint(2,120-2)
                y=random.randint(2,30-2)
                if type <=5 :
                    x_x=random.randint(2,120-2)
                    y_y=random.randint(2,30-2)
                    foodSneak2(x_x,y_y,point)
                else:
                    foodSneak1(x,y,point)

            elif locX==x_x and locY==y_y or locX-1==x_x and locY==y_y or locX-2==x_x and locY==y_y or locX-3==x_x and locY==y_y :
                point -=1
                stack.PopScore()
                x_x=random.randint(2,120-2)
                y_y=random.randint(2,30-2)
                if type <=5 :
                    foodSneak2(x_x,y_y,point)
                else:
                    x=random.randint(2,120-2)
                    y=random.randint(2,30-2)
                    foodSneak1(x,y,point)
            locY = locY - 1
        elif key == KEY_DOWN:
            conta=0
            win.addch(locY,locX-3,' ')
            win.addch(locY,locX-2,' ')
            win.addch(locY,locX-1,' ')
            if locX==x and locY==y or locX-1==x and locY==y or locX-2==x and locY==y or locX-3==x and locY==y :
                point+=1
                stack.PushScore(x,y)
                x=random.randint(2,120-2)
                y=random.randint(2,30-2)
                if type <=5 :
                    x_x=random.randint(2,120-2)
                    y_y=random.randint(2,30-2)
                    foodSneak2(x_x,y_y,point)
                else:

                    foodSneak1(x,y,point)
            elif locX==x_x and locY==y_y or locX-1==x_x and locY==y_y or locX-2==x_x and locY==y_y or locX-3==x_x and locY==y_y  :
                point -=1
                stack.PopScore()
                x_x=random.randint(2,120-2)
                y_y=random.randint(2,30-2)
                if type <=5 :
                    foodSneak2(x_x,y_y,point)
                else:
                    x=random.randint(2,120-2)
                    y=random.randint(2,30-2)
                    foodSneak1(x,y,point)
            locY = locY + 1

        elif key==27:
            queue.ScoreEnqueue(str(name),point)
            print("---------")
            win.clear()
            win.timeout(0)
            menuOption()
        elif key==53:
            if conta==0:
                stack.printStack()
                stack.generearDoc()
                conta+=1
        elif key==54:
            if conta==0:
                queue.printValue()
                conta+=1

        win.addch(locY,locX,'#')
        win.addch(locY,locX-1,'#')
        win.addch(locY,locX-2,'#')
def moveUser():
    new = cir.returnFirst()
    win.clear()
    win.border(0)
    stdscr.clear()
    key =0
    while key!=27:
        win.addstr(2, 30,"Move User")
        key = win.getch()

        if key==KEY_LEFT:
            win.clear()
            win.border(0)
            win.refresh()
            new = new.prev
            win.addstr(5, 30,new.name)
        elif key==KEY_RIGHT:
            win.clear()
            win.border(0)
            win.refresh()
            win.addstr(5, 30,new.name)
            new = new.next
        elif key==27:
            win.clear()
            win.refresh()
            menuOption()
        elif key==10:
            win.clear()
            win.refresh()
            playGame(new.prev.name)
        else:
            curses.endwin
def foodSneak2(x,y,point):
    win.addstr(0,65, 'Points: '+ str(point))
    win.addstr(y,x, "*")

def foodSneak1(x,y,point):
    win.addstr(0,65, 'Points: '+ str(point))
    win.addstr(y,x, "+")
def obtainName():

    win.clear()
    win.border(0)
    win.addstr(10, 10,"Your Name")
    curses.echo()
    curses.curs_set(1)
    input = win.getstr(11,10).decode(encoding="utf-8")

    if cir.isFind(input)==False:
        cir.addUser(input)
    playGame(input)
def obtainOption2():

    win.clear()
    win.border(0)
    win.addstr(7,21, '1. UserReports')
    win.addstr(8,21, '2. ScoreBoardReports')
    curses.echo()
    curses.curs_set(1)
    input2 = win.getstr(10,21).decode(encoding="utf-8")

    if int(input2)==1:
        print(input2)
        cir.generateImage()
        menuOption()
    elif int(input2)==2:
        queue.GenerateImage()
        menuOption()
def showUser():
    cont=10
    win.clear()
    win.border(0)
    win.addstr(9, 10,"Name")
    win.addstr(9, 18,"Score")
    aux = queue.getFirst()
    while aux!=None:
        win.addstr(cont, 10,str(aux.name))
        win.addstr(cont, 18,str(aux.points))
        cont+=1
        aux=aux.next
def menuOption():
    curses.curs_set(0)
    curses.noecho()
    win.clear()
    stdscr.addstr(10, 10,"Hola")
    win.addstr(7,21, '1. Play')
    win.addstr(8,21, '2. Scoreboard')
    win.addstr(9,21, '3. User Selection')
    win.addstr(10,21, '4. Reports')
    win.addstr(11,21, '5. Bulk Loading')
    win.addstr(12,21, '6. Exit')
    win.border(0)
    while 1:
        key = win.getch()
        if key==51:
            win.clear()
            win.border(0)
            win.addstr(2, 30,"Move")
            moveUser()
        elif key==50:
            showUser()
        elif key==52:
            obtainOption2()
        elif key==49:
            obtainName()
        elif key==53:
            x=""
            win.clear()
            win.border(0)
            win.addstr(2, 30,"Bulk Loading")
            win.addstr(7,21, 'Insert Path of file')
            curses.echo()
            curses.curs_set(1)
            input2 = win.getstr(9,21).decode(encoding="utf-8")
            f = open(input2,'r',encoding = 'utf-8')
            if f.mode == "r":
                contents = f.read()
                cont = contents.split("\n")

            conta = 1

            while conta<len(cont):
                cir.addUser(cont[conta])
                conta+=1
        elif key==27:
            win.clear()
            curses.curs_set(0)
            menuOption()

        elif key==54:
            win.clear()
            break


menuOption()
