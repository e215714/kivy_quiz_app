from model import Model
from view import View


class Controller():
    def __init__(self, _model: Model, _view: View) -> None:
        self.view = _view
        self.model = _model
    
    def on_start(self) -> None:
        """クイズを選んで，表示する．
        スタート時に実行する．
        """
        self.model.select_quiz()
        self.view.show_quiz(self.model.quiz_count ,self.model.now_quiz)
    
    def on_select(self, num: int) -> None:
        """選択肢が選ばれたときに実行される．
        判定結果，解説を表示

        Args:
            num (int): 選ばれた選択肢
        """
        judge = self.model.judge(num)
        self.view.show_judge(judge)
        self.view.show_answer(self.model.now_quiz["comment"])
    
    def on_next(self) -> None:
        """次へが押されたときに実行される．
        """
        self.model.next()
        if self.model.is_end:
            self.view.show_result(self.model.correct_num)
        else:
            self.view.show_quiz(self.model.quiz_count, self.model.now_quiz)
    
    def on_restart(self) -> None:
        """はじめに戻るが押されたときに実行される．
        """
        self.model.reset()
        self.view.show_welcome()
    
    def on_exit(self):
        pass