import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.properties import OptionProperty, StringProperty, NumericProperty
from kivy.uix.popup import Popup

from models import lessonInfos

class LessonListScreen(Screen):
    pass
class LessonInfoScreen(Screen):
    lesson_id = NumericProperty(0)
    lesson_state = OptionProperty("Unenrolled", options=["Unenrolled", "Learning", "Finished"])
    name = StringProperty('LessonName')
    lesson_description = StringProperty('lesson_description')
    instructor = StringProperty('instructor')
    action = StringProperty('Enroll')

    def __init__(self, lesson_id=0, **kw):
        super(LessonInfoScreen, self).__init__(**kw)
        self.lesson_id = lesson_id
        self.lesson = lessonInfos[lesson_id]
        self.name = self.lesson.name
        self.lesson_state = self.lesson.lesson_state
        self.instructor = self.lesson.instructor
        self.lesson_description = self.lesson.description
        self.action = self.get_action(self.lesson_state)

    def get_action(self, state):
        match state:
            case 'Unenrolled':
                return 'Enroll'
            case 'Learning':
                return 'Resume'
            case 'Finished':
                return 'Review'
    

class LessonContentScreen(Screen):
    pass

class LessonInfoRV(RecycleView):
    def __init__(self, **kwargs):
        super(LessonInfoRV, self).__init__(**kwargs)
        self.data = [{'lesson_state': str(x.lesson_state), 'name': str(x.name), 'id': x.id} for x in lessonInfos]

class LessonInfoButton(RecycleDataViewBehavior, BoxLayout, Button):
    lesson_id = NumericProperty(0)
    lesson_state = OptionProperty("Unenrolled", options=["Unenrolled", "Learning", "Finished"])
    name = StringProperty('LessonName')
    index = 0

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        self.lesson_state = data['lesson_state']
        self.lesson_id = data['id']
        self.name = data['name']
        print(self.lesson_state, self.name)
        super(LessonInfoButton, self).refresh_view_attrs(rv, index, data)

    def show_info(self, id):
        App.get_running_app().to_lesson_info_screen(id)

class ElearnApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LessonListScreen(name="Lesson List"))
        sm.add_widget(LessonInfoScreen(name="Lesson Information"))
        sm.add_widget(LessonContentScreen(name="Lesson Content"))
        self.sm = sm

        return sm
    
    def to_lesson_info_screen(self, id):
        screen_name = f'lesson info {id}'
        # print('screen_name: ', screen_name)
        if not self.sm.has_screen('screen_name'):
            screen = LessonInfoScreen(lesson_id=id, name=screen_name)
            self.sm.add_widget(screen)
            self.sm.switch_to(screen)
        else:
            self.sm.current = screen_name

if __name__ == '__main__':
    ElearnApp().run()