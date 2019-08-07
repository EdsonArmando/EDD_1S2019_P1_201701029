import sys,os
import curses
import random
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from Structures.CircularDoubleList import Circular_Double_List
from Structures.ScoreStack import Score_Stack
cir = Circular_Double_List()

stdscr = curses.initscr()
win = curses.newwin(30,120,0,0)
curses.noecho()
curses.cbreak()
curses.curs_set(0)
win.keypad(True)
key=KEY_LEFT
def playGame():
    conta=0
    stack = Score_Stack()
    win.refresh()
    win.clear()
    key = win.getch()
    stdscr.clear()
    win.clear()
    curses.curs_set(0)
    point=0
    x=random.randint(2,120-2)
    y=random.randint(2,30-2)
    x_x=random.randint(2,120-2)
    y_y=random.randint(2,30-2)
    win.clear()
    win.border(0)
    key = KEY_RIGHT
    locX = 5
    locY = 5
    foodSneak1(x,y,0)
    foodSneak2(x_x,y_y,0)
    win.addch(locY,locX,'#')
    while 1:
        win.timeout((100 - 20//3)%90)
        if point>=15:
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

                foodSneak1(x,y,point)
            elif locX==x_x and locY==y_y:
                point -=1
                stack.PopScore()
                x_x=random.randint(2,120-2)
                y_y=random.randint(2,30-2)

                foodSneak2(x_x,y_y,point)
            locX = locX + 1
        elif key == KEY_LEFT:
            win.addch(locY,locX-2,' ')
            if locX==x and locY==y:
                point+=1
                stack.PushScore(x,y)
                x=random.randint(2,120-2)
                y=random.randint(2,30-2)

                foodSneak1(x,y,point)
            elif locX==x_x and locY==y_y:
                point -=1
                stack.PopScore()
                x_x=random.randint(2,120-2)
                y_y=random.randint(2,30-2)

                foodSneak2(x_x,y_y,point)
            locX = locX - 1
        elif key == KEY_UP:
            win.addch(locY,locX-3,' ')
            win.addch(locY,locX-2,' ')
            win.addch(locY,locX-1,' ')
            if locX==x and locY==y or locX-1==x and locY==y or locX-2==x and locY==y or locX-3==x and locY==y :
                point+=1
                stack.PushScore(x,y)
                x=random.randint(2,120-2)
                y=random.randint(2,30-2)

                foodSneak1(x,y,point)
            elif locX==x_x and locY==y_y or locX-1==x_x and locY==y_y or locX-2==x_x and locY==y_y or locX-3==x_x and locY==y_y :
                point -=1
                stack.PopScore()
                x_x=random.randint(2,120-2)
                y_y=random.randint(2,30-2)

                foodSneak2(x_x,y_y,point)
            locY = locY - 1
        elif key == KEY_DOWN:
            win.addch(locY,locX-3,' ')
            win.addch(locY,locX-2,' ')
            win.addch(locY,locX-1,' ')
            if locX==x and locY==y or locX-1==x and locY==y or locX-2==x and locY==y or locX-3==x and locY==y :
                point+=1
                stack.PushScore(x,y)
                x=random.randint(2,120-2)
                y=random.randint(2,30-2)

                foodSneak1(x,y,point)
            elif locX==x_x and locY==y_y or locX-1==x_x and locY==y_y or locX-2==x_x and locY==y_y or locX-3==x_x and locY==y_y  :
                point -=1
                stack.PopScore()
                x_x=random.randint(2,120-2)
                y_y=random.randint(2,30-2)

                foodSneak2(x_x,y_y,point)
            locY = locY + 1

        elif key==27:
            win.clear()
            menuOption()
        elif key==53:
            if conta==0:
                stack.printStack()
                stack.generearDoc()
                print('Edson')
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
        stdscr.clear()
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
        else:
            curses.endwin
def foodSneak2(x,y,point):
    win.addstr(0,45, 'User: Edson')
    win.addstr(0,65, 'Points: '+ str(point))
    win.addstr(y,x, "*")

def foodSneak1(x,y,point):
    win.addstr(0,45, 'User: Edson')
    win.addstr(0,65, 'Points: '+ str(point))
    win.addstr(y,x, "+")
def menuOption():

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
            win.clear()
            win.border(0)
            win.addstr(20, 20,"Hola2")
        elif key==49:
            playGame()
            break;
        elif key==53:
            x=""
            win.clear()
            win.border(0)
            win.addstr(2, 30,"Bulk Loading")
            f = open("C:/Users/EG/PycharmProjects/EDD_1S2019_P1_201701029/ususarios.csv",'r',encoding = 'utf-8')
            if f.mode == "r":
                contents = f.read()
                cont = contents.split("\n")

            conta = 1
            while conta<=len(cont)-1:
                cir.addUser(cont[conta])
                conta+=1
        elif key==27:
            win.clear()
            menuOption()

        elif key==54:
            win.clear()
            break


menuOption()
