class View():
    def __init__(self, _ui) -> None:
        self.ui = _ui
    
    def show_welcome(self) -> None:
        """welcome画面を表示する．
        """
        self.ui.select_screen("welcome")
    
    def show_quiz(self, num, quiz) -> None:
        """クイズを表示する．
        modelから現在のクイズデータを受け取って表示する．

        Args:
            quiz : 形式に沿ったjson形式のデータ
        """
        self.ui.set_num_quiz(f"第 {num+1} 問")
        self.ui.set_quiz_text(quiz["question"])
        self.ui.set_selection(quiz["choices"])
        self.ui.select_screen("quiz")
    
    def show_judge(self, judge: bool) -> None:
        """判定結果を表示する．
        正解かどうかをboolで受け取ってそれに応じたテキストを表示する．

        Args:
            judge (bool): 判定結果
        """
        if judge:
            self.ui.set_judge_text("正解！", "red")
            
        else:
            self.ui.set_judge_text("不正解", "blue")
            
    
    def show_answer(self, text: str) -> None:
        """解説文の表示

        Args:
            text (str): 解説文
        """
        self.ui.set_answer_text(text)
        self.ui.select_screen("answer")
    
    def show_result(self, num: int) -> None:
        """リザルト画面を表示する．

        Args:
            num (int): 正解数
        """
        
        self.ui.set_result_text(f"あなたの正解数は{num}/5でした！")
        self.ui.select_screen("result")
