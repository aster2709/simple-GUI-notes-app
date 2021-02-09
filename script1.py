#!/usr/bin/env python3

from tkinter import *
import os


def main_screen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title('YASH')
    Label(text='welcome to my notes app', bg='green', width='300', font=('Calibri', 13)).pack()
    Label(text='').pack()
    Button(text='Login', command=login).pack()
    Label(text='').pack()
    Button(text='Register', command=register).pack()
    screen.mainloop()


def register():
    try:
        screen2.destroy()
    except:
        pass
    global screen1
    global user
    global passw
    screen1 = Toplevel(screen)
    screen1.geometry('300x250')
    screen1.title('REGISTER')
    Label(screen1, text='').pack()
    Label(screen1, text='username*').pack()
    user = Entry(screen1)
    user.pack()
    Label(screen1, text='password*').pack()
    passw = Entry(screen1)
    passw.pack()
    Label(screen1, text='').pack()
    Button(screen1, text='Register', command=register_user).pack()
    Button(screen1, text='back to Login', command=login).pack()


def register_user():
    u = user.get()
    p = passw.get()
    user.delete(0, END)
    passw.delete(0, END)
    if not os.path.exists(u):
        with open(u, 'w') as file:
            file.write(u+'\n'+p+'\n')
            Label(screen1, text='Registration successful, please login', fg='green').pack()
    else:
        Label(screen1, text='user alread exists, please login', fg='red').pack()


def login():
    try:
        screen1.destroy()
    except:
        pass
    global screen2, user1, passw1
    screen2 = Toplevel(screen)
    screen2.geometry('300x300')
    screen2.title('login')
    Label(screen2, text='').pack()
    Label(screen2, text='username').pack()
    user1 = Entry(screen2)
    user1.pack()
    Label(screen2, text='password').pack()
    passw1 = Entry(screen2)
    passw1.pack()
    Label(screen2, text='').pack()
    Button(screen2, text='Login', command=login_verify).pack()
    Button(screen2, text='New user? Register', command=register).pack()


def login_verify():
    global u
    u = user1.get()
    p = passw1.get()
    user1.delete(0, END)
    passw1.delete(0, END)
    a = True
    for i in os.listdir('.'):
        if i == u:
            a = False
            with open(u) as file:
                credentials = file.read().splitlines()
                print(credentials)
                if p == credentials[1]:
                    login_success()
                else:
                    Label(screen2, text='wrong credentials, try again', fg='red').pack()
    if a:
        Label(screen2, text='wrong credentials, try again', fg='red').pack()


def login_success():
    try:
        screen2.destroy()
    except:
        pass
    global screen3
    screen3 = Toplevel(screen)
    screen3.title('active session')
    screen3.geometry('300x250')
    Label(screen3, text=f'logged in user {u}', bg='green',
          width='300', font=('Calibri', 13)).pack()
    Label(screen3, text='').pack()
    Button(screen3, text='create new note', command=create_notes).pack()
    Label(screen3, text='').pack()
    Button(screen3, text='view notes', command=view_notes).pack()
    Label(screen3, text='').pack()
    Button(screen3, text='delete notes', command=delete_notes).pack()
    Label(screen3, text='').pack()
    Label(screen3, text='').pack()
    Button(screen3, text='Logout', bg='white', fg='black', command=lambda: _destroy(screen3)).pack()


def create_notes():
    global screen4, note
    screen4 = Toplevel(screen)
    screen4.title('create notes')
    screen4.geometry('400x400')
    Label(screen3, text='').pack()
    Label(screen4, text='Enter note').pack()
    note = Entry(screen4)
    note.pack()
    Button(screen4, text='SAVE', fg='white', bg='black',
           command=save_and_destroy).pack()
    Button(screen4, text='go back', command=lambda: _destroy(screen4)).pack()


def view_notes():
    screen6 = Toplevel(screen)
    screen6.title('view notes')
    screen6.geometry('400x400')
    count = 1
    bool = True
    with open(u) as file:
        for i, j in enumerate(file):
            if i > 1:
                bool = False
                Label(screen6, text=f'{count}. {j}', width='300').pack()
                count += 1
                Label(screen6, text='').pack()
    if bool:
        Label(screen6, text='No notes to view', fg='red').pack()
    Button(screen6, text='go back', command=lambda: _destroy(screen6)).pack()


def delete_notes():
    global screen7, delete_note
    screen7 = Toplevel(screen)
    screen7.title('delete notes')
    screen7.geometry('400x600')
    count = 1
    bool = True
    Label(screen7, text='Enter note no. to delete', fg='red').pack()
    delete_note = Entry(screen7)
    delete_note.pack()
    Button(screen7, text='submit', command=delnote).pack()
    Label(screen7, text='').pack()
    with open(u) as file:
        for i, j in enumerate(file):
            if i > 1:
                bool = False
                Label(screen7, text=f'{count}. {j}', width='300').pack()
                count += 1
        if bool:
            Label(screen7, text='No notes to view', fg='red').pack()
    Button(screen7, text='go back', command=lambda: _destroy(screen7)).pack()


def delnote():
    screen5 = Toplevel(screen)
    screen5.title('notes deleted')
    screen5.geometry('200x200')
    n = int(delete_note.get())
    delete_note.delete(0, END)
    if 0 < n < 10:
        with open(u) as file:
            lines = file.readlines()
            print(lines)
        with open(u, 'w') as file:
            for line in lines:
                if lines.index(line) != n+1:
                    file.write(line)
        Label(screen5, text=f'Note no.{n} deleted').pack()
        Button(screen5, text='OK', command=lambda: _destroy(screen7, screen5)).pack()


def _destroy(*screen):
    for i in screen:
        i.destroy()


def save_and_destroy():
    n = note.get()
    note.delete(0, END)
    with open(u, 'a') as file:
        file.write(n+'\n')
    screen4.destroy()


main_screen()
