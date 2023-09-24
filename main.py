import tkinter as t
import math as m
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def time_reset():
    global timer
    window.after_cancel(timer)
    head_label.config(text="TIMER", font=(FONT_NAME, 36, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="")
    global REPS
    REPS = 1
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_count():
    global REPS, LONG_BREAK_MIN, SHORT_BREAK_MIN
    if REPS % 2 != 0:
        start_timer(WORK_MIN*60)
        REPS += 1
        head_label.config(text="WORK", fg=GREEN)
    elif REPS % 2 == 0 and REPS % 8 == 0:
        start_timer(LONG_BREAK_MIN*60)
        REPS += 1
        head_label.config(text="L_BREAK", fg=RED)
    else:
        start_timer(SHORT_BREAK_MIN*60)
        REPS += 1
        head_label.config(text="S_BREAK", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def start_timer(count):
    min_count = m.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    if min_count < 10:
        min_count = f"0{min_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, start_timer, count-1)
    else:
        start_count()
        mark = ""
        work_sessions = m.floor(REPS/2)
        for _ in range(work_sessions-1):
            mark += "✅"
        tick_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = t.Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = t.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = t.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

head_label = t.Label(text="TIMER", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
tick_label = t.Label()

head_label.grid(row=0, column=1)
tick_label.grid(row=3, column=1)

start_button = t.Button(text="Start", font=(FONT_NAME, 18, "bold"), command=start_count)
reset_button = t.Button(text="Reset", font=(FONT_NAME, 18, "bold"), command=time_reset)

start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

window.mainloop()
