from models import Session, User, Program, Enrollment

def run_debug_tests():
    session = Session()
    
    print("\n--- Debugging Angaza Consultants CLI Database ---\n")
    
   
    print("Deleting existing test data...")
    session.query(Enrollment).delete()
    session.query(Program).delete()
    session.query(User).delete()
    session.commit()
    
 
    user1 = User(name="Alice Johnson", email="alice@example.com")
    user2 = User(name="Bob Smith", email="bob@example.com")
    session.add_all([user1, user2])
    session.commit()
    print(f"Created Users: {user1}, {user2}")
    
    
    prog1 = Program(title="Full Stack Web Development", description="Learn to build web apps.")
    prog2 = Program(title="Data Science Bootcamp", description="Become a data expert.")
    session.add_all([prog1, prog2])
    session.commit()
    print(f"Created Programs: {prog1}, {prog2}")
    
  
    enrollment1 = Enrollment(user_id=user1.id, program_id=prog1.id)
    session.add(enrollment1)
    session.commit()
    print(f"Enrolled {user1.name} in {prog1.title}")
    
   
    print(f"\nEnrollments for {user1.name}:")
    enrollments = session.query(Enrollment).filter_by(user_id=user1.id).all()
    for e in enrollments:
        print(f"- {e.program.title}")
    
    print("\nUpdating Bob's email...")
    bob = session.query(User).filter_by(name="Bob Smith").first()
    bob.email = "bob.new@example.com"
    session.commit()
    print(f"Bob's new email: {bob.email}")
    
  
    print("\nDeleting Data Science Bootcamp program...")
    session.delete(prog2)
    session.commit()
    
    print("\nRemaining programs:")
    programs = session.query(Program).all()
    for p in programs:
        print(f"- {p.title}")
    
    session.close()
    print("\n--- Debugging complete ---\n")

if __name__ == "__main__":
    run_debug_tests()
