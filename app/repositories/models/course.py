from app.domain.entities.course import Course


class CourseModel:
    def __init__(self, data):
        self.name = data["name"]

    @staticmethod
    def from_entity(course: Course):
        return CourseModel({
            "name": course.name
        })

    def to_entity(self):
        return Course(name=self.name)

    def to_dict(self):
        return {"name": self.name}
