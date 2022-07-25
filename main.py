import random
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import StringProperty, ListProperty
import japanize_kivy


from model import Model
from view_controller import View, Controller

Window.size = (600, 400)

class WelcomeScreen(Screen):
    pass

class QuizScreen(Screen):
    text =  StringProperty("quiz text")
    selection = ListProperty(["sel_1", "sel_2", "sel_3", "sel_4"])

class AnswerScreen(Screen):
    text = StringProperty("answer text")
    judge = StringProperty("answer text")

class ResultScreen(Screen):
    text = StringProperty("result text")
        

class QuizApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        model = Model()
        self.view = View(model, self)
        self.controller = Controller(model, self.view)
        
    def build(self):
        # Create the screen manager
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(WelcomeScreen(name='welcome'))
        self.sm.add_widget(QuizScreen(name='quiz'))
        self.sm.add_widget(AnswerScreen(name='answer'))
        self.sm.add_widget(ResultScreen(name='result'))
        self.view.show_welcome()
        return self.sm

    def select_screen(self, name: str):
        self.sm.current = name
    
    def set_quiz_text(self, text: str):
        self.sm.get_screen("quiz").text = text
    
    def set_selection(self, texts: list):
        self.sm.get_screen("quiz").selection = texts
    
    def set_answer_text(self, text: str):
        self.sm.get_screen("answer").text = text
    
    def set_judge_text(self, text: str):
        self.sm.get_screen("answer").judge = text
    
    def set_result_text(self, text: str):
        self.sm.get_screen("result").text = text
    
    

if __name__ == "__main__":
    QuizApp().run()