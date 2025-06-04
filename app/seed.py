from models import Session, User, Program, Enrollment

def seed_data():
    session = Session()

    
    session.query(Enrollment).delete()
    session.query(Program).delete()
    session.query(User).delete()
    session.commit()

  
    users = [
        User(name="Alice Johnson", email="alice@example.com",),
        User(name="Bob Smith", email="bob@example.com",),
        User(name="Charlie Brown", email="charlie@gail.com",),
        User(name="Catherine Lee", email="catherine@example.com", ),
        User(name="David Kim", email=" david@gmail.com", ),
        User(name="Eva Green", email="eva@gmail.com", ),
    ]
    session.add_all(users)
    session.commit()
    print(f"Seeded {len(users)} users.")

  
    programs = [
        Program(title="Mucuna development", description="lorem."),
        Program(title="Soya Youth program", description="lorem ipsum dolor sit amet, consectetur adipiscing elit."),
        Program(title="Avacado program", description="Lorem."),
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
