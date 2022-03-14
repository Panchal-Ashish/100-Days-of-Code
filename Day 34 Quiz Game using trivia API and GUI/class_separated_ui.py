from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self,quiz_brain: QuizBrain):   # after (:), we specify the datatype to be taken as input
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(bg= THEME_COLOR, padx= 20, pady= 20)


        self.score_label = Label(text= f"score: {self.score}",font= ("arial",14), bg= THEME_COLOR, fg= "white")
        self.score_label.grid(row= 0, column= 1)


        self.canvas = Canvas(width= 300, height= 250,bg= "white")
        self.question_text = self.canvas.create_text(150,125, text= f"dummy text",
                                                     width= 280, font= ("arial",20,"italic")) # width is to wrap text in definite area
        self.canvas.grid(row= 1, column= 0, columnspan= 2,pady= 50)


        tick_img = PhotoImage(file= "./images/true.png")
        self.tick_button = Button(width= 80, height= 80,image= tick_img, highlightthickness= 0,command= self.true_pressed)
        self.tick_button.grid(row= 2, column= 0)


        cross_img = PhotoImage(file= "./images/false.png")
        self.cross_button = Button(width= 80, height= 80,image= cross_img, highlightthickness= 0,command = self.false_pressed)
        self.cross_button.grid(row=2, column= 1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz"
                                                            f"\n your final score was {self.score}/10")
            self.tick_button.config(state= "disabled")
            self.cross_button.config(state="disabled")


    def true_pressed(self):
        is_correct = self.quiz.check_answer("true")
        if is_correct:
            self.score += 1
            self.window.after(1000)
            self.canvas.config(bg= "green")
            self.score_label.config(text= f"score:{self.score}")

        else:
            self.window.after(1000)
            self.canvas.config(bg= "red")

        self.window.after(1000,func= self.get_next_question)


    def false_pressed(self):
        is_correct = self.quiz.check_answer("false")
        if is_correct:
            self.score += 1
            self.window.after(1000)
            self.canvas.config(bg= "green")
            self.score_label.config(text=f"score: {self.score}")

        else:
            self.window.after(1000)
            self.canvas.config(bg= "red")

        self.window.after(1000,func= self.get_next_question)