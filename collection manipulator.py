print("Welcome to the Student Data Organizer!")
all_Student=[]
total=0
while(True):
        print("\nSelect an option: ")
        print("1. Add Student ")
        print("2. Display All Student")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")
    
        Choice=int(input("Enter your Choice :"))
        match Choice:
            case 1:
                print("\nEnter Student details:")
                total+=1
                record={
                    "Student ID" : total,
                    "Name":input("Enter Name: "),
                    "Age":int(input("Enter Age: ")),
                    "Grade":input("Enter Grade: "),
                    "Date of Bith":input("Enter Date of Birth(YYY-MM-DD): "),
                    "Subjects":set(input("Enter Subjects (comma-separated): ").split(",")),
    
                }
                all_Student.append(record)
                print("\nStudent added successfully!")
    
            case 2:
                for data in all_Student:
                    print(data)

            case 3:
                print("\nUpdate Student Information")
                Student_ID = int(input("Enter Student ID to update: "))
    
                for record in all_Student:
                    if record["Student ID"] == Student_ID:
                        print("Current Student Details:", record)
                        record["Age"] = int(input("New age: "))
                        subs = input("New subjects (comma-separated): ").split(",")
                        record["Subjects"] = {s.strip() for s in subs}
                        print("Student updated successfully!")
                        break

                else:
                    print("Student ID not found.")
   
            case 4:
                print("\nDelete Student")
                Student_ID = int(input("Enter student ID to delete: "))

                for record in all_Student:
                    if record["Student ID"] == Student_ID:
                        all_Student.remove(record)
                        print("Student deleted successfully.")
                        break
                else:
                    print("Student ID not found.")

            case 5:
                Subjects = set()

                for record in all_Student:
                    for s in record["Subjects"]:
                        Subjects.add(s)
                print("\n--- Subjects Offered ---")
                for s in Subjects:
                    print(s)

            case 6:
                print("Thank you for using the Student Data Organizer. Goodbye!")
                break
            
            case _:
             print("Invalid choice.")