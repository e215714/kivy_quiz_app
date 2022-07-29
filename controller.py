from model import Model
from view import View


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