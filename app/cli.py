from app.helpers import display_welcome, display_main_menu, login_or_register, browse_programs, view_enrollments, enroll_in_program

def main():
    print(" Welcome to Angaza Consultants CLI \n")

    while True:
        print("Please choose an option:")
        print("1. Create user")
        print("2. List programs")
        print("3. Enroll user in a program")
        print("4. View user enrollments")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            create_user(name, email)

        elif choice == "2":
            list_programs()

        elif choice == "3":
            try:
                user_id = int(input("Enter user ID: "))
                program_id = int(input("Enter program ID: "))
                enroll_user(user_id, program_id)
            except ValueError:
                print("Invalid input. IDs must be numbers.")

        elif choice == "4":
            try:
                user_id = int(input("Enter user ID: "))
                view_user_enrollments(user_id)
            except ValueError:
                print("Invalid input. User ID must be a number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()

