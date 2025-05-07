from enum import Enum

class Role(Enum):
    STUDENT = "Student"
    PROFESSOR = "Professor"

class User:
    def __init__(self, name, email, number):
        self.name = name
        self.email = email
        self.number = number

        self.role = Role.STUDENT if 7>2 else Role.PROFESSOR
