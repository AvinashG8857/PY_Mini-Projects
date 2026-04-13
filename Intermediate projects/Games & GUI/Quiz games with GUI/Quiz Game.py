import tkinter as tk

questions=[
    {
        "question":"What is the capital of INDIA?",
        "options":["Mumbai","Delhi","Kolkatta","CHennai"] ,
        "answer":"Delhi"
    },
    {
        "question":"Which language is used for AI?",
        "options": ["Python","C++","Java","HTML"],
        "answer":"Python"
    },
    {
        "question":"Who developed the theory of relativity?",
        "options": ["Newton","Einstein","Tesla","Edison"],
        "answer":"Einstein"
    }
]

class QuizGame:
    def __init__(self,root):
        self.root= root
        self.root.title("Quiz Game")
        self.scrore=0
        self.q_index=0

        self.question_label=tk.Label(root,text="",font=("Arial",16))
        self.question_label.pack(pady=20)
        self.buttons=[]
        for i in range(4):
            btn= tk.Button(root,text="",font=("Arial",14),width=20,command=lambda i=i: self.check_answers(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.next_button = tk.Button(root,text="Next Question", command=self.next_question)
        self.next_button.pack(pady=20)

        self.result_label= tk.Label(root, text="",font=("Arial",14))
        self.result_label.pack(pady=10)
        self.load_questions()
    
    def load_questions(self):
        if self.q_index<len(questions):
            q= questions[self.q_index]
            self.question_label.config(text=q["question"])
            for i,option in enumerate(q["options"]):
                self.buttons[i].config(text=option)
            self.result_label.config(text="")
        else:
            self.question_label.config(text="Quiz Over!")
            for btn in self.buttons:
                btn.pack_forget()
            self.next_button.pack_forget()
            self.result_label.config(text=f"Final Score: {self.scrore}/{len(questions)}")

    def check_answers(self,i):
        q= questions[self.q_index]
        if q["options"][i] == q["answer"]:
            self.scrore+=1
            self.result_label.config(text="Correct!",fg= "green")
        else:
            self.result_label.config(text=f"Wrong! Answer: {q['answer']}",fg="red")

    def next_question(self):
        self.q_index+=1
        self.load_questions()

root= tk.Tk()
game= QuizGame(root)
root.mainloop()