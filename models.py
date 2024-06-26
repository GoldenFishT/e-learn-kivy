import random
class Lesson:
    pass

STATES = ["Unenrolled", "Learning", "Finished"]

class LessonInfo:
    _id = 0

    def __init__(self, name, lesson_state, instructor=None, tags=None, description=None) -> None:
        self.id = LessonInfo._id
        LessonInfo._id += 1
        self.name = name
        self.lesson_state = lesson_state
        self.instructor = instructor if instructor else 'instructor name'
        self.tags = tags if tags else []
        self.description = description if description else ""

    def set_description(self, description):
        self.description = description

    def __repr__(self):
        return str(self.name)
    
        

class LessonContent:
    pass
    


TAGS = ['math', 'computer', 'science', 'geometry', 'analysis', 'algorithm', 'introduction']

lessonInfos = [
    LessonInfo(name=f'lesson name{i}', lesson_state=random.choice(STATES), tags=random.sample(TAGS, random.randint(0, len(TAGS)))) for i in range(20)
]