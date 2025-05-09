import checker
import typer
from user import User, Role

# Start the database with mock data
_users: list[User] = [
    User("Simon Gomez", "simon.gomez@utv.edu.co", "+57 123 456 7890", Role.STUDENT),
    User("Santiago Yepes", "santiago.yepes@utv.edu.co", "+57 098 765 4321", Role.STUDENT),
    User("Sofia Aristizabal", "sofia.aristizabal@utv.edu.co", "+57 567 438 9210", Role.PROFESSOR)
]

def register_user(name: str, email: str, number: str):
    if not checker.is_valid_name(name):  raise ValueError("Invalid name")
    if not checker.is_valid_number(number):  raise ValueError("Invalid Number")

    user_role = checker.classify_email(email)

    if user_role == 0:  raise ValueError("Invalid Email")
    if user_role == 1:  user = User(name, email, number, Role.PROFESSOR)
    else:  user = User(name, email, number, Role.STUDENT)

    _users.append(user)


def get_all_users() -> list[str]:
    return _users.copy()


def get_all_students() -> list[User]:
    return [user for user in _users if user.role == Role.STUDENT]


def get_all_professors() -> list[User]:
    return [user for user in _users if user.role == Role.PROFESSOR]


def search_user_by_email(email: str) -> list[User]:
    return [user for user in _users if checker.is_partial_email(email, user.email)]
