import tkinter as tk
from tkinter import messagebox
import random

# Sample quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Jupiter"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy"],
        "correct_answer": "William Shakespeare"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.color = ['#FF6F61', '#6B4226', '#D9BF77']
        self.current_question = 0
        self.score = 0

        self.welcome_frame = tk.Frame(root)
        self.welcome_frame.pack()

        self.welcome_label = tk.Label(self.welcome_frame, text="Welcome to the Quiz Game!", font=("Helvetica", 20), fg=self.color[0])
        self.welcome_label.pack(pady=20)

        self.start_button = tk.Button(self.welcome_frame, text="Start Quiz", font=("Helvetica", 14), fg="white", bg=self.color[1], command=self.start_quiz)
        self.start_button.pack(pady=10)

        self.load_quiz_frame = tk.Frame(root)

        self.question_label = tk.Label(self.load_quiz_frame, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            option_button = tk.Button(self.load_quiz_frame, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(option_button)
            option_button.pack(pady=5)

        self.next_question_button = tk.Button(self.load_quiz_frame, text="Next Question", font=("Helvetica", 12), command=self.load_next_question)
        self.next_question_button.pack(pady=10)
        self.next_question_button.config(state="disabled")

        self.feedback_label = tk.Label(self.load_quiz_frame, text="", font=("Helvetica", 12), fg=self.color[0])
        self.feedback_label.pack(pady=10)

        self.load_quiz_frame.pack_forget()
        self.load_next_question()

    def start_quiz(self):
        self.welcome_frame.pack_forget()
        self.load_quiz_frame.pack()
        self.load_next_question()

    def load_next_question(self):
        if self.current_question < len(questions):
            self.current_question += 1
            question_obj = questions[self.current_question - 1]
            self.question_label.config(text=question_obj["question"], fg=self.color[0])
            random.shuffle(question_obj["options"])
            for i, option_button in enumerate(self.option_buttons):
                option_button.config(text=question_obj["options"][i], state="normal", fg=self.color[2], bg=self.color[1])
            self.next_question_button.config(state="disabled")
            self.feedback_label.config(text="", fg=self.color[0])
        else:
            self.show_final_results()

    def check_answer(self, user_choice):
        question_obj = questions[self.current_question - 1]
        user_answer = question_obj["options"][user_choice]
        correct_answer = question_obj["correct_answer"]
        if user_answer == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct! Well done.", fg=self.color[0])
        else:
            self.feedback_label.config(text=f"Sorry, the correct answer is: {correct_answer}", fg=self.color[0])
        self.next_question_button.config(state="active")

    def show_final_results(self):
        self.question_label.config(text="Quiz Completed!", fg=self.color[0])
        for option_button in self.option_buttons:
            option_button.config(state="disabled")
        self.next_question_button.config(text="Quit", command=self.root.quit, fg=self.color[0], bg=self.color[1])
        final_score = (self.score / len(questions)) * 100
        result_text = f"Your Score: {self.score}/{len(questions)}\nPerformance: {final_score:.2f}%"
        self.feedback_label.config(text=result_text, fg=self.color[0])

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
