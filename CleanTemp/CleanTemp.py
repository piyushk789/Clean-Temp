#   Clean Temp
#   Author : Kartikey Baghel
#   Mail   : kartikeybaghel@hotmail.com

""" Simple-Easy process to clean Temporary File."""

import ctypes, sys, os, shutil

FolderOpen = False
k = {'file': 0, 'folder': 0, 'error': 0}

def clean(j:str):
    for i in os.listdir(j):
            if os.path.isfile(f'{j}/{i}'): k["file"] += 1
            if os.path.isdir(f'{j}/{i}'): k["folder"] += 1
            try: os.remove(f'{j}/{i}')
            except:
                try: shutil.rmtree(f'{j}/{i}')
                except: k["error"] += 1

def RunAsAdmin():
    for loc in ["C:\\Windows\\Temp", f"C:\\Users\\{os.getlogin()}\\Appdata\\Local\\Temp"]: clean(loc)
    if ctypes.windll.shell32.IsUserAnAdmin(): clean("C:\\Windows\\Prefetch")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        clean("C:\\Windows\\Prefetch")
    print(k["file"])
    print(k["folder"])
    print(k["error"])

if __name__ == '__main__':
    RunAsAdmin()
    if FolderOpen:
        for i in [f"C:\\Users\\{os.getlogin()}\\Appdata\\Local\\Temp", "C:\\Windows\\Temp", "C:\\Windows\\Prefetch"]: os.startfile(i)