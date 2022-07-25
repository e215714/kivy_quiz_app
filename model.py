import json
import random


class Model():
    def __init__(self):
        self.quiz_data = []
        self.selected_quiz_data = []
        self.correct_num = 0
        self.lim_num = 5
        self.quiz_count = 0
        self.now_num = 0  # not used
        self.now_quiz = {}  # added
        self.is_end = False  # added
        
        with open("./quiz.json", encoding="utf-8") as f:
            self.quiz_data = json.load(f)["quiz"]
    
    def judge(self, num: int):
        if self.now_quiz["answer"] == num:
            self.increment_correct()
            return True
        else:
            return False
    
    def next(self):  # added
        self.increment_count()
        if self.quiz_count >= self.lim_num:
            self.is_end = True
        else:
            self.now_quiz = self.selected_quiz_data[self.quiz_count]
    
    def reset(self):  # added
        self.selected_quiz_data = []
        self.correct_num = 0
        self.quiz_count = 0
        self.now_quiz = {}
        self.is_end = False
    
    def increment_correct(self) -> None:
        self.correct_num += 1
    
    def increment_count(self) -> None:
        self.quiz_count += 1
    
    def select_quiz(self):
        self.selected_quiz_data = random.sample(self.quiz_data, k=self.lim_num)
        self.now_quiz = self.selected_quiz_data[self.quiz_count]
        