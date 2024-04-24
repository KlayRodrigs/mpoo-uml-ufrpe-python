from CourseEntity import CourseEntity
from TeacherEntity import TeacherEntity


class CoordinatorEntity(CourseEntity, TeacherEntity):
    def __init__(self, courseName):
        super().__init__(courseName)

    def __str__(self):
        return f"Coordinator at: "
    
coordinatorEntity = CoordinatorEntity("Bacharelado em Sistemas de Informação")
print(coordinatorEntity)