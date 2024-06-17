def func() :
    price = 0
    if cv1.get()==1 :
        price+=5000
    if cv2.get()==1 :
        price+=6000
    if cv3.get()==1 :
        price+=12000
    label.config(text = "가격 :"+str(price)+"원")

import tkinter
import tkinter.font

window = tkinter.Tk()
window.title('음식 계산기')
window.geometry('300x200+100+100')

title_font = tkinter.font.Font(family = "맑은 고딕", size = 20)
title = tkinter.Label(window, text = "음식 계산기", font = title_font)
title.grid(row=0,column=0,columnspan=4)

label = tkinter.Label(window, text = "가격 : 0원",font = title_font)
label.grid(row=3,column=0,columnspan=4)

cv1 = tkinter.IntVar()
cv2 = tkinter.IntVar()
cv3 = tkinter.IntVar()

check1 = tkinter.Checkbutton(window, variable=cv1, command=func)
check2 = tkinter.Checkbutton(window, variable=cv2, command=func)
check3 = tkinter.Checkbutton(window, variable=cv3, command=func)

img_1 = tkinter.PhotoImage(file="짜장면.png")
img_2 = tkinter.PhotoImage(file="짬뽕.png")
img_3 = tkinter.PhotoImage(file="탕수육.png")
img_label1 = tkinter.Label(window, image=img_1)
img_label2 = tkinter.Label(window, image=img_2)
img_label3 = tkinter.Label(window, image=img_3)

check1.grid(row=1,column=0)
check2.grid(row=1,column=2)
check3.grid(row=2,column=0)
img_label1.grid(row=1,column=1)
img_label2.grid(row=1,column=3)
img_label3.grid(row=2,column=1)

window.mainloop()