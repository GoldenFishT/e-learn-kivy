import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior 
from kivy.properties import OptionProperty, StringProperty
from kivy.uix.popup import Popup

from models import lessonInfos

class LessonInfoRV(RecycleView):
    def __init__(self, **kwargs):
        super(LessonInfoRV, self).__init__(**kwargs)
        self.data = [{'lesson_state': str(x.lesson_state), 'name': str(x.name)} for x in lessonInfos]

class LessonInfoButton(RecycleDataViewBehavior, BoxLayout, Button):
    lesson_state = OptionProperty("Unenrolled", options=["Unenrolled", "Learning", "Finished"])
    name = StringProperty('LessonName')
    index = 0

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        self.lesson_state = data['lesson_state']
        self.name = data['name']
        print(self.lesson_state, self.name)
        super(LessonInfoButton, self).refresh_view_attrs(rv, index, data)

    def show_info(self):
        the_content = Label(text="coming soon!")
        popup = Popup(title='Lesson Information', content=the_content,
                      size_hint=(.6, .3))
        popup.open()


class ElearnApp(App):
    def build(self):
        return LessonInfoRV()

if __name__ == '__main__':
    ElearnApp().run()