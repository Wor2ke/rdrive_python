from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from servo import Servo

def clicked_ok():
    global var
    koeficient = var.get()
    print(koeficient)
def interface(INTERFACE_NAME, SERVO_1_ID, logger):
    dec = Servo(INTERFACE_NAME, SERVO_1_ID, logger)
    window = Tk()
    oves = 10.0
    ris = 6.8
    grecha = 4.1
    psheno = 3.9
    roj = 16.8
    goroh = 11.7
    speed = 5
    temp = 40
    A = 8
    V = 220
    var = DoubleVar()
    window.title("БрГТУ")
    window.geometry('800x500')
    btn_start = Button(window, text="Старт", bg="blue", fg="white", font=("Arial Bold", 15), command=lambda :dec.start(1, logger), padx=50, pady=50).place(x=60, y=40)
    btn_stop = Button(window, text="Стоп", bg="blue", fg="white", font=("Arial Bold", 15), command= lambda :dec.stop(), padx=50, pady=50).place(x=300, y=40)
    lbl = Label(window, text="Введите необходимый коэфициент:", font=("roboto", 14)).place(x=60, y=220)
    entry = Entry(window, width=20, textvariable=var).place(x=60, y=270)
    ok_btn = Button(window, text="Ok", bg="blue", fg="white", font=("Arial Bold", 10), command=clicked_ok, padx=10, pady=10).place(x=190, y=260)
    lbl_crups = Label(window, text="Известные коэфициенты:", font=("roboto", 14)).place(x=500, y=220)

    lbl_oves = Label(window, text="Овес:", font=("roboto", 14)).place(x=500, y=250)
    lbl_oves_speed = Label(window, text=str(oves), font=("roboto", 14)).place(x=660, y=250)

    lbl_ris = Label(window, text="Рис:", font=("roboto", 14)).place(x=500, y=280)
    lbl_ris_speed = Label(window, text=str(ris), font=("roboto", 14)).place(x=660, y=280)

    lbl_grecha = Label(window, text="Гречка:", font=("roboto", 14)).place(x=500, y=310)
    lbl_grecha_speed = Label(window, text=str(grecha), font=("roboto", 14)).place(x=660, y=310)

    lbl_psheno = Label(window, text="Пшено:", font=("roboto", 14)).place(x=500, y=340)
    lbl_psheno_speed = Label(window, text=str(psheno), font=("roboto", 14)).place(x=660, y=340)

    lbl_roj = Label(window, text="Рожь:", font=("roboto", 14)).place(x=500, y=370)
    lbl_roj_speed = Label(window, text=str(roj), font=("roboto", 14)).place(x=660, y=370)

    lbl_goroh = Label(window, text="Горох:", font=("roboto", 14)).place(x=500, y=400)
    lbl_goroh_speed = Label(window, text=str(goroh), font=("roboto", 14)).place(x=660, y=400)

    lbl_char = Label(window, text="Основные характеристики:", font=("roboto", 14)).place(x=500, y=30)

    lbl_speed = Label(window, text="Скорость(об/мин):", font=("roboto", 14)).place(x=500, y=60)
    lbl_speed_char = Label(window, text=str(speed), font=("roboto", 14)).place(x=720, y=60)

    lbl_tempriture = Label(window, text="Температура(Гр.):", font=("roboto", 14)).place(x=500, y=90)
    lbl_temp_char = Label(window, text=str(temp), font=("roboto", 14)).place(x=720, y=90)

    lbl_A = Label(window, text="Ток(А):", font=("roboto", 14)).place(x=500, y=120)
    lbl_A_char = Label(window, text=str(A), font=("roboto", 14)).place(x=720, y=120)

    lbl_V = Label(window, text="Напряжение(В):", font=("roboto", 14)).place(x=500, y=150)
    lbl_V_char = Label(window, text=str(V), font=("roboto", 14)).place(x=720, y=150)

    window.mainloop()

