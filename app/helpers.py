from models import Session, User, Program, Enrollment
from sqlalchemy.exc import IntegrityError
import re

current_user = None

def display_welcome():
    print("\n" + "=" * 50)
    print("Welcome to Angaza Consultants!")
    print("=" * 50)
    print("Empowering your future through our diverse training programs.")
    print("=" * 50 + "\n")

def display_main_menu():
    print("\nMain Menu:")
    print("1. Login / Register")
    print("2. Browse Programs")
    print("3. View My Enrollments")
    print("4. Enroll in a Program")
    print("5. Logout")
    print("6. Exit")
    return input("Select an option (1-6): ").strip()

def login_or_register():
    global current_user
    session = Session()
    
    print("\nUser Authentication")
    print("1. Login")
    print("2. Register")
    choice = input("Choose (1-2): ").strip()
    
    if choice == '1':
        email = input("Enter your email: ").strip()
        user = session.query(User).filter_by(email=email).first()
        if user:
            current_user = user
            print(f"Welcome back, {user.name}!")
        else:
            print("User not found. Please register.")
    
    elif choice == '2':
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format.")
            session.close()
            return
        
        existing = session.query(User).filter_by(email=email).first()
        if existing:
            print("Email already registered. Please login.")
            session.close()
            return
        
        new_user = User(name=name, email=email)
        session.add(new_user)
        try:
            session.commit()
            current_user = new_user
            print(f"Registration successful! Welcome, {new_user.name}!")
        except IntegrityError:
            session.rollback()
            print("Error during registration. Try again.")
    
    session.close()

def browse_programs():
    session = Session()
    programs = session.query(Program).all()
    
    print("\nAvailable Programs:")
    print("=" * 50)
    print(f"{'ID':<5} {'Title':<30} {'Description'}")
    print("=" * 50)
    for p in programs:
        print(f"{p.id:<5} {p.title:<30} {p.description}")
    print("=" * 50)
    
    session.close()

def view_enrollments():
    global current_user
    if not current_user:
        print("Please login to view your enrollments.")
        return
    
    session = Session()
    enrollments = session.query(Enrollment).filter_by(user_id=current_user.id).all()
    
    if not enrollments:
        print("You are not enrolled in any programs yet.")
    else:
        print(f"\nPrograms enrolled by {current_user.name}:")
        print("=" * 50)
        for e in enrollments:
            print(f"- {e.program.title}")
        print("=" * 50)
    
    session.close()

def enroll_in_program():
    global current_user
    if not current_user:
        print("Please login before enrolling.")
        return
    
    program_id = input("Enter the Program ID you want to enroll in: ").strip()
    
    session = Session()
    program = session.query(Program).filter_by(id=program_id).first()
    
    if not program:
        print("Program not found.")
        session.close()
        return
    

    existing = session.query(Enrollment).filter_by(user_id=current_user.id, program_id=program.id).first()
    if existing:
        print(f"You are already enrolled in '{program.title}'.")
        session.close()
        return
    
        enrollment = Enrollment(user_id=current_user.id, program_id=program.id)
    session.add(enrollment)
    try:
        session.commit()
        print(f"Successfully enrolled in '{program.title}'.")
    except:
        session.rollback()
        print("Enrollment failed. Please try again.")

    session.close()

