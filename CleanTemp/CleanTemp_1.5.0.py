#   Clean Temp
#   Author : Kartikey Baghel
#   Mail   : kartikeybaghel@hotmail.com

""" Simple-Easy process to clean Temporary File."""

import ctypes, sys, os, shutil, winshell
from tkinter import Tk, Label, Button, Checkbutton, BooleanVar

logo = r"C:\Users\piyush\Documents\VS_Code_Data\Python\My VS Files\Python Into Exe\Output_folder\logo.ico"
screen = Tk()
screen.title('Clean Temporary File - PK')
screen['bg'] = '#222'
screen.iconbitmap(logo)
screen.geometry('500x400')
screen.minsize(500, 400)
screen.resizable(False, False)

var = BooleanVar()

k = {'File': 0, 'Folder': 0, "Can't Delete": 0}
err = [[],[]]

def clean(j:str):
    try:
        for i in os.listdir(j):
            if os.path.isfile(f'{j}/{i}'): k["File"] += 1
            if os.path.isdir(f'{j}/{i}'): k["Folder"] += 1
            try: os.remove(f'{j}/{i}')
            except:
                try: shutil.rmtree(f'{j}/{i}')
                except PermissionError as pe:
                    k["Can't Delete"] += 1
                    err[0].append(pe)
                except Exception as e:
                    err[1].append(e)
                    k["Can't Delete"] += 1
    except PermissionError as mainPE:
        k["Can't Delete"] += 1
        err[0].append(mainPE)

def RunAsAdmin() -> list:
    for loc in ["C:\\Windows\\Temp", os.environ['TMP'], winshell.recent()]: clean(loc)

    if ctypes.windll.shell32.IsUserAnAdmin(): clean("C:\\Windows\\Prefetch")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        clean("C:\\Windows\\Prefetch")

    if var.get():
        try: winshell.recycle_bin().empty(False)
        except Exception as e: pass #print(e)
    return [k['File'], k['Folder'], k["Can't Delete"], err]


def TF():
    screen.resizable(False, True)
    screen.maxsize(500, 500)
    screen.geometry('500x500')
    value = RunAsAdmin()
    file.config(text=f'File : {value[0]}', fg='#fff')
    folder.config(text=f'Folder : {value[1]}', fg='#fff')
    error.config(text=f"Can't Delete : {value[2]}", fg='#fff')
    global k, err
    k = {'File': 0, 'Folder': 0, "Can't Delete": 0}
    err = [[],[]]


DESCRIPTION = """"Clean Temp" is an application designed to help users efficiently clean up temporary files and folders from their computer. Temporary files are created by various applications and processes on a computer and are intended to be used for a short period of time. However, these files can accumulate over time, taking up valuable disk space and slowing down the computer's performance.\nThe "Clean Temp" application provides a simple and user-friendly interface that allows users to quickly scan their computer for temporary files and folders. Once the scan is complete, the application presents a list of all temporary files and folders found, along with their file size and location."""

Label(screen, text=DESCRIPTION, bg=screen['bg'], fg='#fff', font='times 14 italic', wraplength=500).pack(side='top', anchor='center')
Label(screen, text='It is secure and save to use.', bg=screen['bg'], fg='#f55', font='rounded 16').pack(side='top', pady=10)

Button(screen, text='Clean up', bg='#f60', command=TF, font='times 16', activebackground='#0f0').pack()
Checkbutton(screen, text='Clean Recycle Bin', variable=var, bg=screen['bg'], font='times 16', activebackground='#0f0', onvalue=True, offvalue=False).pack(pady=5, padx=5)

file = Label(screen, text='File : 0', bg=screen['bg'], fg=screen['bg'], font='arial 14')
file.pack(side='bottom', anchor='w')
folder = Label(screen, text='Folder : 0', bg=screen['bg'], fg=screen['bg'], font='arial 14')
folder.pack(side='bottom', anchor='w')
error = Label(screen, text="Can't Delete : 0", bg=screen['bg'], fg=screen['bg'], font='arial 14')
error.pack(side='bottom', anchor='w')

screen.mainloop()