import random
class Lesson:
    pass

STATES = ["Unenrolled", "Learning", "Finished"]

class LessonInfo:
    

    def __init__(self, name, lesson_state, tags=None) -> None:
        self.name = name
        self.lesson_state = lesson_state
        self.tags = tags

    def __repr__(self):
        return str(self.name)
    
        

class LessonContent:
    pass

TAGS = ['math', 'computer', 'science', 'geometry', 'analysis', 'algorithm', 'introduction']

lessonInfos = [
    LessonInfo(name=f'lesson name{i}', lesson_state=random.choice(STATES), tags=random.sample(TAGS, random.randint(1, len(TAGS)))) for i in range(20)
]