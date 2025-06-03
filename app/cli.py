from app.db import SessionLocal
from app.models import User, Program

session = SessionLocal()

def update_user(user_id, new_name=None, new_email=None):
    user = session.query(User).get(user_id)
    if not user:
        print("User not found.")
        return

    if new_name:
        user.name = new_name
    if new_email:
        user.email = new_email

    session.commit()
    print("User updated successfully.")


def update_program(program_id, new_name=None, new_description=None):
    program = session.query(Program).get(program_id)
    if not program:
        print("Program not found.")
        return

    if new_name:
        program.name = new_name
    if new_description:
        program.description = new_description

    session.commit()
    print("Program updated successfully.")


def enroll_user(user_id, program_id):
    user = session.query(User).get(user_id)
    program = session.query(Program).get(program_id)

    if not user or not program:
        print("User or program not found.")
        return

    if program not in user.programs:
        user.programs.append(program)
        session.commit()
        print(f"{user.name} has been enrolled in {program.name}.")
    else:
        print(f"{user.name} is already enrolled in {program.name}.")


def unenroll_user(user_id, program_id):
    user = session.query(User).get(user_id)
    program = session.query(Program).get(program_id)

    if program in user.programs:
        user.programs.remove(program)
        session.commit()
        print(f"{user.name} has been unenrolled from {program.name}.")
    else:
        print(f"{user.name} is not enrolled in {program.name}.")
