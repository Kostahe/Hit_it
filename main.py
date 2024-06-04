from turtle import *
from time import *
from random import *

hideturtle()

Turtle
t = Turtle()
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t3.hideturtle()
t1.hideturtle()
t2.hideturtle()
t2.penup()
t1.penup()
t3.penup()
t1.goto(100, 110)
t3.goto(100, 130)
z = 0

t1.write('Points:', font=('Arial', 15, 'normal'))
t2.goto(160, 110)
t2.write(z, font=('Arial', 15, 'normal'))

t3.write('Goal:10', font=('Arial', 15, 'normal'))
t.color('red')
t.shape('turtle')
t.points = 0


def rand_move():
    t.penup()
    x = randint(-100, 100)
    y = randint(-100, 100)
    t.goto(x, y)


def catch(x, y):
    global z

    t.points += 1
    rand_move()
    z += 1
    t2.clear()
    t2.write(z, font=('Arial', 15, 'normal'))
    # tpoints


t.points = 0
t.onclick(catch)
while t.points != 10:
    sleep(1.5)
    rand_move()
    t.onclick(catch)
    if t.points >= 10:
        t.clear()
        break

if t.points == 10:
    color('green')
    penup()
    goto(-75, 0)
    write('WOW YOU DIT IT!', font=('Arial', 20, 'normal'))
    hideturtle()
    t.hideturtle()
if t.points == 11:
    color('green')
    penup()
    goto(-75, 0)
    write('WOW YOU DID IT AND IT GLITCHED IT!', font=('Arial', 20, 'normal'))
    hideturtle()
if t.points >= 12:
    color('green')
    penup()
    goto(-75, 0)
    write('WOW YOU DID IT AND GLITCHED IT MORE!', font=('Arial', 20, 'normal'))
    hideturtle()
    t.hideturtle()

Harder_mode = input('Harder mode maybe?')
Harder_mode = Harder_mode.lower()
if Harder_mode != 'yes' and Harder_mode != 'no':
    print('Yes or no only')

if Harder_mode == 'no':
    print('Okay thank you for that you were playing bye :) ')
if Harder_mode == 'yes':
    t3.clear()
    t.showturtle()
    t1.clear()
    clear()
    t2.clear()
    z = 0
    t1.write('Points:', font=('Arial', 15, 'normal'))

    t2.write(z, font=('Arial', 15, 'normal'))
    t3.write('Goal:15', font=('Arial', 15, 'normal'))
    t.color('red')
    t.shape('turtle')
    z = 0
    t.points = 0
    while t.points != 15:

        sleep(0.85)
        rand_move()
        t.onclick(catch)
        if t.points >= 15:
            t.clear()
            break
    if t.points == 15:
        color('green')
        penup()
        goto(-75, 0)
        write('WOW YOU DIT IT AGAIN!', font=('Arial', 20, 'normal'))
        hideturtle()
    if t.points == 16:
        clear()
        color('green')
        penup()
        goto(-75, 0)
        write('WOW YOU IT AGAIN BUT GLITCHED IT!!', font=('Arial', 20, 'normal'))
        hideturtle()
    if t.points >= 17:
        clear()
        color('green')
        penup()
        goto(-75, 0)
        write('WOW YOU DID IT AGAIN BUT YOU GLITCHED IT MORE!!', font=('Arial', 20, 'normal'))
        hideturtle()
    t.hideturtle()

    Hardest_mode = input('Hardest mode?')
    Hardest_mode = Hardest_mode.lower()
    if Hardest_mode == 'no':
        print('Oke you did good thank you for that you were playing byeeeeee ;)')

    if Hardest_mode == 'yes':
        t.showturtle()
        clear()
        t2.clear()
        t3.clear()
        z = 0
        t1.write('Points:', font=('Arial', 15, 'normal'))

        t2.write(z, font=('Arial', 15, 'normal'))
        t3.write('Goal:20', font=('Arial', 15, 'normal'))
        t.color('red')
        t.shape('turtle')

        t.points = 0
        while t.points != 20:

            sleep(0.25)
            rand_move()
            t.onclick(catch)
            if t.points >= 20:
                t.clear()
                break
        if t.points == 20:
            color('green')
            penup()
            goto(-75, 0)
            write('WOW YOU ARE PRO!', font=('Arial', 20, 'normal'))
            hideturtle()
        if t.points == 21:
            color('green')
            penup()
            goto(-75, 0)
            write('WOW YOU ARE GLITCHER!', font=('Arial', 20, 'normal'))
            hideturtle()
        if t.points >= 22:
            color('red')
            penup()
            goto(-75, 0)
            write('WOW YOU ARE PRO IN GLITCHING!', font=('Arial', 20, 'normal'))

        IMPOSIBLE_MODE = input('IMPOSIBLE MODE?')
        IMPOSIBLE_MODE = IMPOSIBLE_MODE.lower()
        if IMPOSIBLE_MODE == 'no':
            print('Okey pro player thank you for that you were playing byeeeeee ;) ')
        if IMPOSIBLE_MODE != 'yes' and Harder_mode != 'no':
            print('Yes or no only')
        if IMPOSIBLE_MODE == 'yes':
            t.showturtle()
            clear()
            t2.clear()
            t3.clear()
            z = 0
            t1.write('Points:', font=('Arial', 15, 'normal'))

            t2.write(z, font=('Arial', 15, 'normal'))
            t3.write('Goal:30', font=('Arial', 15, 'normal'))
            t.color('red')
            t.shape('turtle')

            t.points = 0
            while t.points != 30:

                sleep(0.1)
                rand_move()
                t.onclick(catch)
                if t.points >= 30:
                    t.clear()
                    break
            if t.points == 30:
                color('green')
                penup()
                goto(-75, 0)
                write('Imposible...you did it you win!', font=('Arial', 20, 'normal'))
                hideturtle()
                print('Great job idk how you did it but you are pro player if you want secret level write in comments')
            if t.points == 31:
                color('green')
                penup()
                goto(-75, 0)
                write('WOW YOU ARE IMPOSIBLE GLITCHER!', font=('Arial', 20, 'normal'))
                hideturtle()
            if t.points >= 32:
                color('red')
                penup()
                goto(-75, 0)
                write('WOW YOU ARE IMPOSSIBLE PRO IN GLITCHING!', font=('Arial', 20, 'normal'))
            t.hideturtle()
            exitonclick()





