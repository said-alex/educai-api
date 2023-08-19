from uuid import UUID, uuid4

class Course:
    def __init__(
        self,
        name: str,
        course_id: UUID = uuid4(),
    ):
        self.id = course_id
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Course):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
