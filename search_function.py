from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


locations = ["hello", "goodbye"]
App.title = "sanguine"


class Send(FloatLayout):
    def __int__(self):
        super(Send, self).__init__()

    def send_message(self):
        msg = self.search.text
        self.search.text = ""


class SearchFunction(App):
    def build(self):
        return Send()


search = SearchFunction()
search.run()