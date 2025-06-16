class Student:
    schoolName = "ABC"

    def __init__(self, a, b):
        self.name = a
        self.roll_no = b

    def display(self):
        print("Name : ",self.name,"Roll No : ",self.roll_no,"School : ", Student.schoolName)


def main():
    obj1 = Student("Rohit", 8)
    obj2 = Student("Ritu", 9)

    obj1.display()
    obj2.display()

    Student.School_Name = "GS"

    print("Change school name")

    obj1.display()
    obj2.display()

if __name__ == "__main__":
    main()