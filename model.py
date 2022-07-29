import json
import random


class Model():
    def __init__(self) -> None:
        self.quiz_data = []  # クイズデータ
        self.selected_quiz_data = []  # 選んだクイズデータ
        self.correct_num = 0  # 正解数
        self.lim_num = 5  # 問題数
        self.quiz_count = 0  # 何問目か
        self.now_quiz = {}  # 現在のクイズ
        self.is_end = False  # 終了状態か
        
        # 同階層のクイズデータ(json)の読み込み
        with open("./quiz.json", encoding="utf-8") as f:
            self.quiz_data = json.load(f)["quiz"]
    
    def judge(self, num: int) -> bool:
        """現在の問題の正解と引数の数字を比較する．

        Args:
            num (int): 判定したい数字

        Returns:
            bool: 正解かどうか
        """
        if self.now_quiz["answer"] == num:
            self.correct_num += 1
            return True
        else:
            return False
    
    def next(self) -> None:
        """状態を次へ移行する
        quiz_countをインクリメントして，lim_numを超えたら終了状態に．
        超えていなければnow_quizに次の問題をセット．
        """
        # self.increment_count()
        self.quiz_count += 1
        if self.quiz_count >= self.lim_num:
            self.is_end = True
        else:
            self.now_quiz = self.selected_quiz_data[self.quiz_count]
    
    def reset(self) -> None:
        """初期状態に戻す
        クイズデータの再読み込みはしない．
        """
        self.selected_quiz_data = []
        self.correct_num = 0
        self.quiz_count = 0
        self.now_quiz = {}
        self.is_end = False
    
    def select_quiz(self):
        """クイズを選択する．
        quiz_dataからlim_numぶん，クイズを選択する．
        now_quizに最初の問題をセット．
        """
        self.selected_quiz_data = random.sample(self.quiz_data, k=self.lim_num)
        self.now_quiz = self.selected_quiz_data[self.quiz_count]
        