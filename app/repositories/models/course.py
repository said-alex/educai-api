from app.domain.entities.course import Course

class CourseModel:
    def __init__(self, data):
        self.name = data["name"]

    def to_entity(self):
        return Course(name=self.name)
