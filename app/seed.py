from models import Session, User, Program, Enrollment

def seed_data():
    session = Session()

    
    session.query(Enrollment).delete()
    session.query(Program).delete()
    session.query(User).delete()
    session.commit()

  
    users = [
        User(name="Alice Johnson", email="alice@example.com", phone="0712345678"),
        User(name="Bob Smith", email="bob@example.com", phone="0723456789"),
        User(name="Catherine Lee", email="catherine@example.com", phone="0734567890"),
    ]
    session.add_all(users)
    session.commit()
    print(f"Seeded {len(users)} users.")

  
    programs = [
        Program(title="Full Stack Web Development", description="Learn to build dynamic websites and APIs."),
        Program(title="Data Science Bootcamp", description="Master data analysis, visualization, and machine learning."),
        Program(title="Cybersecurity Fundamentals", description="Learn the basics of securing networks and systems."),
    ]
    session.add_all(programs)
    session.commit()
    print(f"Seeded {len(programs)} programs.")

   
    enrollments = [
        Enrollment(user_id=users[0].id, program_id=programs[0].id),
        Enrollment(user_id=users[1].id, program_id=programs[1].id),
        Enrollment(user_id=users[2].id, program_id=programs[2].id),
        Enrollment(user_id=users[0].id, program_id=programs[2].id),
    ]
    session.add_all(enrollments)
    session.commit()
    print(f"Seeded {len(enrollments)} enrollments.")

    session.close()
    print("Seeding complete.")

if __name__ == "__main__":
    seed_data()
