import sys,os
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
from Structures.CircularDoubleList import Circular_Double_List
cir = Circular_Double_List()

stdscr = curses.initscr()
win = curses.newwin(30,70,0,0)
curses.noecho()
curses.cbreak()
win.keypad(True)
key=KEY_LEFT
def moveUser():
    new = cir.returnFirst()
    while 1:
        win.addstr(2, 30,"Move User")
        key = win.getch()
        stdscr.clear()
        if key==KEY_LEFT:
            win.border(0)
            new = new.prev
            win.addstr(5, 30,new.name)
        elif key==KEY_RIGHT:
            win.clear()
            win.border(0)
            win.addstr(5, 30,new.name)
            new = new.next
        elif key==27:
            win.clear()
            menuOption()
        else:
            win.clear()
            menuOption()

def menuOption():
    win.clear()
    stdscr.addstr(10, 10,"Hola")
    win.addstr(7,21, '1. Play')             #paint option 1
    win.addstr(8,21, '2. Scoreboard')       #paint option 2
    win.addstr(9,21, '3. User Selection')   #paint option 3
    win.addstr(10,21, '4. Reports')         #paint option 4
    win.addstr(11,21, '5. Bulk Loading')    #paint option 5
    win.addstr(12,21, '6. Exit')
    win.border(0)
    while 1:
        key = win.getch()
        stdscr.clear()
        if key==49:
            win.border(0)
            win.addstr(10, 10,"Hola")
        elif key==51:
            win.clear()
            win.border(0)
            win.addstr(2, 30,"Move User")
            moveUser()
        elif key==50:
            win.clear()
            win.border(0)
            win.addstr(20, 20,"Hola2")
        elif key==53:
            x=""
            win.clear()
            win.border(0)
            win.addstr(2, 30,"Bulk Loading")
            f = open("C:/Users/EG/PycharmProjects/EDD_2S2019_P1_201701029/ususarios.csv",'r',encoding = 'utf-8')
            if f.mode == "r":
                contents = f.read()
                cont = contents.split("\n")

            conta = 1
            while conta<=len(cont)-1:
                cir.addUser(cont[0])
                conta+=1
        elif key==27:
            win.clear()
            menuOption()
        else:
            break
    curses.endwin()

menuOption()
