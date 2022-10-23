from tkinter import *
import random
import math

paragraphs = ["It was difficult for him to admit he was wrong. He had been so certain that he was correct and the "
              "deeply held belief could never be shaken. Yet the proof that he had been incorrect stood right "
              "before his eyes. 'See daddy, I told you that they are real!' his daughter excitedly proclaimed.",
              "Twenty-five stars were neatly placed on the piece of paper. There was room for five more stars but "
              "they would be difficult ones to earn. It had taken years to earn the first twenty-five, "
              "and they were considered the 'easy' ones.",
              "Things aren't going well at all with mom today. She is just a limp noodle and wants to sleep all "
              "the time. I sure hope that things get better soon.",
              "She wondered if the note had reached him. She scolded herself for not handing it to him in person. "
              "She trusted her friend, but so much could happen. She waited impatiently for word.",
              "It probably seemed trivial to most people, but it mattered to Tracey.She wasn't sure why it mattered"
              "so much to her, but she understood deep within her being that it mattered to her. So for the 365th"
              "day in a row, Tracey sat down to eat pancakes for breakfast."]
timer_on = None
para = ""


def time(count):
    # counting the number of seconds and minutes from the variable count
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    elif minutes < 10:
        minutes = f"0{minutes}"
    return f"{minutes}:{seconds}"


def countdown(count):
    global timer_on
    time_remaining = time(count)
    timer.config(text=time_remaining)
    if count > 0:
        timer_on = window.after(1000, countdown, count - 1)
    else:
        user_answer = text.get("1.0", END)
        window.after_cancel(timer_on)
        text.grid_forget()
        text.delete("1.0", END)
        timer.grid_forget()
        # adding the woeds per minute and accuracy logic
        wpm = (len(user_answer)/5)/0.5
        acc = 0
        for i in range(len(user_answer)):
            try:
                if para[i] == user_answer[i]:
                    acc += 1
            except IndexError:
                acc += 0
        accuracy = (acc/len(user_answer))*100
        paragraph_label.config(text=f"RESULT:\nSpeed: {wpm} WPM , Accuracy: {accuracy}%")
        button.grid(row=4, column=1, pady=15)
        timer.grid(row=0, column=3)


def generate_paragraph():
    global para
    button.grid_forget()
    text.delete("1.0", END)
    text.focus()
    text.grid(row=5, column=1, columnspan=2, padx=58)
    countdown(30)
    para = random.choice(paragraphs)
    paragraph_label.config(text=para)


# GUI
window = Tk()
window.minsize(width=650, height=450)
window.title("Typing Speed Test")
window.config(bg="#404040")

title_label = Label(text="Typing Speed Test", bg="#404040", font=("Arial", 25), fg="white")
title_label.grid(row=0, column=0, columnspan=3)

instruction_label = Label(text="Test your speed using the paragraph given below!", bg="#404040", font=("Courier", 15), fg="white")
instruction_label.grid(row=1, column=0, columnspan=3, padx=30, pady=30)

paragraph_label = Label(text="", bg="#404040", font=("Arial", 12), fg="white", wraplength=400, justify="center")
paragraph_label.grid(row=2, column=0, rowspan=2, columnspan=3, pady=15)

button = Button(text="Start", width=14, command=generate_paragraph, relief="groove")
button.grid(row=4, column=1, pady=15)

timer = Label(text="", bg="#404040", font=("Arial", 20), fg="white")
timer.grid(row=0, column=3)

text = Text(height=2, width=80)

window.mainloop()
