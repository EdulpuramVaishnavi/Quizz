import tkinter as tk
from tkinter import messagebox

class QuestionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Question App")

        self.questions = [
            "What is the capital of France?",
            "What is the largest planet in our solar system?",
            "Who wrote 'Romeo and Juliet'?",
            "What is RAM?",
        ]

        self.answers = ["Paris", "Jupiter", "William Shakespeare","Random Access memory"]
        self.user_responses = []

        self.current_question = 0

        self.label = tk.Label(master, text=self.questions[self.current_question])
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        user_answer = self.entry.get()
        correct_answer = self.answers[self.current_question]

        self.user_responses.append({"Question": self.questions[self.current_question], "User Answer": user_answer})

        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect!", f"Correct answer is: {correct_answer}")

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.label.config(text=self.questions[self.current_question])
            self.entry.delete(0, tk.END)
        else:
            self.show_summary()

    def show_summary(self):
        summary = "Summary:\n"
        for response in self.user_responses:
            summary += f"{response['Question']} - Your Answer: {response['User Answer']}\n"

        messagebox.showinfo("Quiz Completed", summary)
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuestionApp(root)
    root.mainloop()
