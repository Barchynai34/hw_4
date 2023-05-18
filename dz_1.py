#ДЗ №1
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Меня зовут {self.fullname}. Мне {self.age} лет. {'Я не женат.'}")


person = Person("Осмонов Данияр", 18, True )
person.introduce_myself()

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)

student = Student("Осмонов Данияр", 25, False, {"Математика": 5, "литература": 3, "Физика": 4})
student.introduce_myself() 
print(student.calculate_average_mark())

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def calculate_salary(self):
        base_salary = self.salary
        if self.experience > 3:
            bonus = (self.experience - 3) * 5 * base_salary
            return base_salary + bonus
        else:
            return base_salary

    def info(self):
        print(f"Меня зовут {self.fullname}. Мне {self.age} лет. {'Я не женат.'}")

teacher = Teacher("Осмонов Данияр", 25, False, 6 ,80000)
print(teacher.calculate_salary())


def create_students():
    student1 = Student("Эргешов Кыял", 16, False, {"иностранный язык": 2, "химия": 4, "литература": 5})
    student2 = Student("кадыров Элдияр", 17, False, {"иностранный язык": 5, "химия": 4, "литература": 4})
    student3 = Student("Иванов Даут", 18, False, {"иностранный язык": 5, "химия": 5, "литература": 3})
    return [student1, student2, student3]


students = create_students()
for student in students:
    student.introduce_myself()
    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")
    average_mark = student.calculate_average_mark()
    print(f"Average mark: {average_mark:2f}")
    


