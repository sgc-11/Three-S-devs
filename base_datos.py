import checker
import typer
from user import User, Role

_users: list[User] = list()

def register_user(name: str, email: str, number: str):
    if not checker.is_valid_name(name):  raise ValueError("Invalid name")
    if not checker.is_valid_number(number):  raise ValueError("Invalid Number")

    user_role = checker.classify_email(email)

    if user_role == 0:  raise ValueError("Invalid Email")
    if user_role == 1:  user = User(name, email, number, Role.PROFESSOR)
    else:  user = User(name, email, number, Role.STUDENT)

    _users.append(user)


def get_all_emails() -> list[str]:
    return [user.email for user in _users]


def get_all_students() -> list[User]:
    return [user for user in _users if user.role == Role.STUDENT]


def get_all_professors() -> list[User]:
    return [user for user in _users if user.role == Role.PROFESSOR]
