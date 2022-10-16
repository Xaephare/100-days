from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_counter = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score_counter.grid(column=1, row=0)

        self.question_box = Canvas(width=300, height=250)
        self.question_text = self.question_box.create_text(150,
                                                           125,
                                                           text="ya mum",
                                                           font=FONT,
                                                           fill=THEME_COLOR,
                                                           width=280)
        self.question_box.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_img,
                                  highlightthickness=0,
                                  command=lambda: self.quiz.check_answer("True"))
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img,
                                   highlightthickness=0,
                                   command=lambda: self.quiz.check_answer("False"))
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.question_box.itemconfig(self.question_text, text=q_text)
