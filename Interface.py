from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from servo import Servo


def clicked_ok():
    global var
    koeficient = var.get()
    print(koeficient)


def interface(INTERFACE_NAME, SERVO_1_ID, logger):
    servo_obj = Servo(INTERFACE_NAME, SERVO_1_ID, logger)
    servo_obj1 = Servo("Ker", 228, logger)

    if id(servo_obj) == id(servo_obj1):
        print("Same instance")
    
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
    
    Button(window, text="Старт", bg="blue", fg="white", font=("Arial Bold", 15), command=lambda : servo_obj.start(1, logger), padx=50, pady=50).place(x=60, y=40)
    Button(window, text="Стоп", bg="blue", fg="white", font=("Arial Bold", 15), command= lambda : servo_obj.stop(logger), padx=50, pady=50).place(x=300, y=40)
    
    Label(window, text="Введите необходимый коэфициент:", font=("roboto", 14)).place(x=60, y=220)
    Entry(window, width=20, textvariable=var).place(x=60, y=270)
    Button(window, text="Ok", bg="blue", fg="white", font=("Arial Bold", 10), command=clicked_ok, padx=10, pady=10).place(x=190, y=260)
    Label(window, text="Известные коэфициенты:", font=("roboto", 14)).place(x=500, y=220)

    Label(window, text="Овес:", font=("roboto", 14)).place(x=500, y=250)
    Label(window, text=str(oves), font=("roboto", 14)).place(x=660, y=250)

    Label(window, text="Рис:", font=("roboto", 14)).place(x=500, y=280)
    Label(window, text=str(ris), font=("roboto", 14)).place(x=660, y=280)

    Label(window, text="Гречка:", font=("roboto", 14)).place(x=500, y=310)
    Label(window, text=str(grecha), font=("roboto", 14)).place(x=660, y=310)

    Label(window, text="Пшено:", font=("roboto", 14)).place(x=500, y=340)
    Label(window, text=str(psheno), font=("roboto", 14)).place(x=660, y=340)

    Label(window, text="Рожь:", font=("roboto", 14)).place(x=500, y=370)
    Label(window, text=str(roj), font=("roboto", 14)).place(x=660, y=370)

    Label(window, text="Горох:", font=("roboto", 14)).place(x=500, y=400)
    Label(window, text=str(goroh), font=("roboto", 14)).place(x=660, y=400)

    Label(window, text="Основные характеристики:", font=("roboto", 14)).place(x=500, y=30)

    Label(window, text="Скорость(об/мин):", font=("roboto", 14)).place(x=500, y=60)
    Label(window, text=str(speed), font=("roboto", 14)).place(x=720, y=60)

    Label(window, text="Температура(Гр.):", font=("roboto", 14)).place(x=500, y=90)
    Label(window, text=str(temp), font=("roboto", 14)).place(x=720, y=90)

    Label(window, text="Ток(А):", font=("roboto", 14)).place(x=500, y=120)
    Label(window, text=str(A), font=("roboto", 14)).place(x=720, y=120)

    Label(window, text="Напряжение(В):", font=("roboto", 14)).place(x=500, y=150)
    Label(window, text=str(V), font=("roboto", 14)).place(x=720, y=150)

    window.mainloop()

