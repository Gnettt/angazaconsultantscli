from helpers import display_welcome, display_main_menu, login_or_register, browse_programs, view_enrollments, enroll_in_program

def main():
    display_welcome()
    login_or_register()

    while True:
        choice = display_main_menu()
        
        if choice == "1":
            login_or_register()
        elif choice == "2":
            browse_programs()
        elif choice == "3":
            view_enrollments()
        elif choice == "4":
            enroll_in_program()
        elif choice == "5":
            print("Logging out...\n")
            from helpers import current_user
            current_user = None
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()


