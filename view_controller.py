from model import Model


class View():
    def __init__(self, _model: Model, _ui):
        self.model = _model
        self.ui = _ui
    
    def show_welcome(self):
        self.ui.select_screen("welcome")
    
    def show_quiz(self):
        quiz = self.model.now_quiz
        self.ui.set_quiz_text(quiz["question"])
        self.ui.set_selection(quiz["choices"])
        self.ui.select_screen("quiz")
    
    def show_judge(self, text):
        self.ui.set_judge_text(str(text))
    
    def show_answer(self, text):
        self.ui.set_answer_text(text)
        self.ui.select_screen("answer")
    
    def show_result(self):
        self.ui.set_result_text(f"あなたの正解数は{self.model.correct_num}/5でした！")
        self.ui.select_screen("result")

class Controller():
    def __init__(self, _model: Model, _view: View):
        self.view = _view
        self.model = _model
    
    def on_start(self):
        self.model.select_quiz()
        self.view.show_quiz()
    
    def on_select(self, num: int):
        judge = self.model.judge(num)
        self.view.show_judge(judge)
        self.view.show_answer(self.model.now_quiz["comment"])
    
    def on_next(self):
        self.model.next()
        if self.model.is_end:
            self.view.show_result()
        else:
            self.view.show_quiz()
    
    def on_restart(self):
        self.model.reset()
        self.view.show_welcome()
    
    def on_exit(self):
        pass
    