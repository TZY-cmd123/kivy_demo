from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
# https://www.jianshu.com/p/f95576c03f5b
Builder.load_string('''
<OneScreen>
    Label:
        text: "My mother screen was created by kv and python codes."
''')
# 以上的kv代码代表窗口
class OneScreen(Screen):
    pass

class TestApp(App):
    def build(self):
        return OneScreen()

TestApp().run()