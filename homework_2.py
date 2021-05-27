# 1) Создайте класс, описывающий человека (создайте метод, выводящий информацию о человеке).
# 2) На его основе создайте класс Студент (переопределите метод вывода информации).
# 3) Создайте класс Группа, который содержит массив из 10 объектов класса Студент.
# Реализуйте методы добавления, удаления студента и метод поиска студента по фамилии. Определите для
# Группы метод __str__() для возвращения списка студентов в виде строки.
class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_info(self):
        print(f'I am human, my name: {self.name}, surname: {self.surname}, age: {self.age}')


class Student(Human):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def print_info(self):
        print(f'I am student, my name: {self.name}, surname: {self.surname}, age: {self.age}')

    def __str__(self):
        return f'name: {self.name}, surname: {self.surname}, age: {self.age}'


class Group:
    def __init__(self, student_list=None):
        if student_list is None:
            student_list = []
        self.student_list = student_list
        self.student_dict = {student.surname: student for student in student_list}

    def add_student(self, student: Student):
        self.student_list.append(student)
        self.student_dict[student.surname] = student

    def delete_student(self, student: Student):
        self.student_list.remove(student)
        del self.student_dict[student.surname]

    def find_by_surname(self, surname):
        return self.student_dict.get(surname)

    def __str__(self):
        return str(list(map(str, self.student_list)))


if __name__ == '__main__':
    student_1 = Student('Leva', 'Rossum', 18)
    student_2 = Student('Levvvva', 'Rosssssssum', 20)
    group_1 = Group([student_1])
    group_1.add_student(student_2)
    print(group_1)
    group_1.delete_student(student_1)
    print(group_1)
    student_3 = Student('Levvvva', 'hjfjckyt', 20)
    group_1.add_student(student_3)
    print(group_1)
    print(group_1.find_by_surname('hjfjckyt'))

