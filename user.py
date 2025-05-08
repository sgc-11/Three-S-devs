from enum import Enum

class Role(Enum):
    STUDENT = "Student"
    PROFESSOR = "Professor"

class User:
    def __init__(self, name: str, email: str, number: str, role: Role):
        self.name = name
        self.email = email
        self.number = number
        self.role = role

