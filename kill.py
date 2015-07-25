# coding:utf-8

__author__ = 'Dima'
import subprocess,time,datetime

from tkinter import *






def check():
    # проверка времени - если 0 - 6, вырубить комп
    now_time = datetime.datetime.now()
    cur_hour = now_time.hour # Час текущий

    if (1 < cur_hour and cur_hour < 8):


        root = Tk()
        root.geometry('1280x1024')

        for i in reversed(range(0,100)):

            root.configure(background  ="red")

            lab = Label(root,text = "компьютер выключится через%s секунд" % i,background = "red",foreground ="white",font='Arial 120')
            lab.place(x=200, y=400)


            root.update()

            time.sleep(0.01)

            if i > 5:
                lab.configure(background = "white")


        root.mainloop()

        p = subprocess.Popen('shutdown /s /t 0', shell=True)
        p.wait()
        return True
    else:
        return False




while not check():
    print("false")
    time.sleep(3600)
    check()


