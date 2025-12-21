import csv
filename = "students.csv"

class Student:
    def __init__(self, name, roll_no, crs, section, mar1, mar2, mar3, mar4, mar5, mar6, mar7):
        self.name = name
        self.roll_no = roll_no
        self.crs = crs
        self.section = section
        self.mar1 = mar1
        self.mar2 = mar2
        self.mar3 = mar3
        self.mar4 = mar4
        self.mar5 = mar5
        self.mar6 = mar6
        self.mar7 = mar7
        self.avg = round((mar1 + mar2 + mar3 + mar4 + mar5 + mar6 + mar7) / 7, 2)
        self.grade = self.Grade()
 
    def Grade(self):
        if self.avg >= 95:
            return "A+"
        elif self.avg >= 85:
            return "A"
        elif self.avg >= 75:
            return "B"
        elif self.avg >= 65:
            return "C"
        elif self.avg >= 50:
            return "D"
        else:
            return "FAIL"

    def header(self):
        return [self.name, self.roll_no, self.crs, self.section, self.mar1, self.mar2, self.mar3, 
                self.mar4, self.mar5, self.mar6, self.mar7, self.avg, self.grade]

class Choices:
    def __init__(self):
        try:
            with open(filename, "x", newline="") as file: # x means header
                writer = csv.writer(file)
                writer.writerow(["Name", "Roll Number", "Course", "Section", "Math Marks", "Pysics Marks", "Web dev Marks", "Python Marks", "PD Marks", "UHV Marks", "Yoga Marks", "Average Marks", "Grade"])
        except FileExistsError:
            pass

    def AddStudent(self):
        print("=== Add New Student ===\n") 

        name = input("Enter Student's Name: ")
        if not name.replace(" ", "").isalpha():
            print("Error: Name me only alphabets hona chahiye.")
            return

        try:
            roll_no = int(input("Roll Number: "))
        except ValueError:
            print("Error: Roll Number sirf integer value hona chahiye.")
            return 

        crs = input("Course Name: ")
        section = input("Section: ")

        print("==== Enter Subject Marks(0-100) ====\n")
        try:
            mar1 = int(input("Math Marks: "))
            mar2 = int(input("Physics Marks: "))
            mar3 = int(input("Web dev Marks: "))
            mar4 = int(input("Python Marks: "))
            mar5 = int(input("PD Marks: "))
            mar6 = int(input("UHV Marks: "))
            mar7 = int(input("Yoga Marks: "))
        except ValueError:
           print("Error: You cannot enter string in marks, Please enter integer in marks.")
           return

        s = Student(name, roll_no, crs, section, mar1, mar2, mar3, mar4, mar5, mar6, mar7)
        with open(filename, "a", newline="") as file:
            write = csv.writer(file)
            write.writerow(s.header())
            print("*** Student added Successfully ***\n")

    def ViewStudent(self):
        print("==== Students List ====\n")
        try:
            with open(filename, "r") as file:
                read = csv.reader(file)
                for rows in read:
                    print(rows)
        except FileNotFoundError as err:
            print("Students list doesn't exist", err)

    def SearchStudent(self):
        roll = input("Enter Roll Number for Searching a Student: ")
        exist = False

        with open(filename, "r") as file:
            read = csv.reader(file)
            for row in read:
                if row[1] == roll:
                    print("Student exist:", row, "\n")
                    exist = True
                    break
        if not exist:
            print("**This Roll number Student doesnot exist\n")
    
    def DeleteStudent(self):
        roll = input("Enter Roll Number for Delete: ")
        Studentrows = []
        deleted = False
        
        with open(filename, "r") as file:
            read = csv.reader(file)
            for row in read:
                if row[1] == roll:
                    deleted = True
                    continue
                Studentrows.append(row)
        if deleted:
            with open(filename, "w", newline="") as file:
                write = csv.writer(file)
                write.writerows(Studentrows)
            print("*** Student Deleted Successfully ***\n")
        else:
            print("***Student with this Roll Number not found***\n")

    def UpdateStudent(self):
        roll = int(input("Enter Roll Number for Update : "))
        update = False
        Studentdata = []

        # Read all data
        with open(filename, "r") as file:
            read = csv.reader(file)
            header = next(read)
            for row in read:
                Studentdata.append(row)

        # Find student
        for row in Studentdata:
            if int(row[1]) == roll:
                update = True
                print("Student Current Record:", row)

                name = input("Student's New Name: ")
                if not name.replace(" ", "").isalpha():
                   print("Error: Name me only alphabets hona chahiye.")
                   return
                
                new_roll= input("New Roll Number: ")
                crs = input("New Course Name: ")
                section = input("New Section Name: ")
                try:
                    mar1 = int(input("Math New Marks: "))
                    mar2 = int(input("Physics New Marks: "))
                    mar3 = int(input("Web dev New Marks: "))
                    mar4 = int(input("Python New Marks: "))
                    mar5 = int(input("PD New Marks: "))
                    mar6 = int(input("UHV New Marks: "))
                    mar7 = int(input("Yoga New Marks: "))
                except ValueError:
                   print("Error: You cannot enter alphabets in marks, Please enter integer in marks.")
                   return

                avg = round((mar1 + mar2 + mar3 + mar4 + mar5 + mar6 + mar7) / 7, 2)
                if avg >= 95:
                    grade = "A+"
                elif avg >= 85:
                    grade = "A"
                elif avg >= 75:
                    grade = "B"
                elif avg >= 65:
                    grade = "C"
                elif avg >= 50:
                    grade = "D"
                else:
                    grade = "FAIL"

                row[:] = [name, new_roll, crs, section, mar1, mar2, mar3, mar4, mar5, mar6, mar7, avg, grade]
                break

        if not update:
            print("***Not Student exist!\n")
            return
        # Save updated data
        with open(filename, "w", newline="") as file:
            write = csv.writer(file)
            write.writerow(header)
            write.writerows(Studentdata)
        print("***Student updated Successfully***\n")
    
Options = Choices()
while True:
    print("1. Add New Student")
    print("2. View Students List")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    option = input("Choose Options(1/2/3/4/5/6): ")
    if option == "1":
        Options.AddStudent()
    elif option == "2":
        Options.ViewStudent()
    elif option == "3":
        Options.SearchStudent()
    elif option == "4":
        Options.DeleteStudent()
    elif option == "5":
        Options.UpdateStudent()
    elif option == "6":
        print("***Exist from the Student Management data***")
        break
    else:
        print("***Wrong Option, Select options between 1 to 6\n")





