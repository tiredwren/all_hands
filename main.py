from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class WindowManager(ScreenManager):
    pass


sm = WindowManager()  # setting a variable to the window manager class


class LogIn(Screen):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)

class SearchFunction(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Hello(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Goodbye(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Error(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

screens = [LogIn(name="log_in"),SearchFunction(name="search_function"), Hello(name="hello"), Goodbye(name="goodbye"),Error(name="error")]  # setting an array of lists
for screen in screens:  # going through all of the screens
    sm.add_widget(screen)  # adding the screen widget to each

sm.current = "search_function"

App.title = "sanguine"