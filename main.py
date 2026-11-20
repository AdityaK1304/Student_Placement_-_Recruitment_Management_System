
from student import (
    add_student,
    view_students,
    update_student,
    delete_student
)

from company import (
    add_company,
    view_companies
)

from placement import (
    add_placement,
    view_placements
)

from analysis import placement_analysis


def main():

    while True:

        print("\n================================")
        print(" STUDENT PLACEMENT MANAGEMENT ")
        print("================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Company")
        print("6. View Companies")
        print("7. Add Placement")
        print("8. View Placements")
        print("9. Placement Analysis")
        print("10. Exit")

        choice = input("\nEnter Your Choice: ")

        try:
            if choice == "1":
                add_student()

            elif choice == "2":
                view_students()

            elif choice == "3":
                update_student()

            elif choice == "4":
                delete_student()

            elif choice == "5":
                add_company()

            elif choice == "6":
                view_companies()

            elif choice == "7":
                add_placement()

            elif choice == "8":
                view_placements()

            elif choice == "9":
                placement_analysis()

            elif choice == "10":
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Please Enter Valid Input!")


if __name__ == "__main__":
    main()
