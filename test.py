"""Módulo para gestionar estudiantes y sus calificaciones."""

class Student:
    """Representa a un estudiante con sus calificaciones."""

    def __init__(self, student_id, name):
        """Crea un estudiante con su ID y nombre."""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.passed = "NO"
        self.honor = "?"

    def add_grade(self, grade):
        """Agrega una calificación a la lista."""
        self.grades.append(grade)

    def calculate_average(self):
        """Calcula y retorna el promedio de las calificaciones."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Convierte el promedio en una letra de calificación."""
        average = self.calculate_average()
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def check_honor(self):
        """Determina si el estudiante está en el cuadro de honor."""
        if self.calculate_average() >= 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """Elimina una calificación por su índice."""
        del self.grades[index]

    def report(self):
        """Imprime el reporte del estudiante."""
        print("ID: " + str(self.student_id))
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Average: " + str(self.calculate_average()))
        print("Final Grade = " + self.get_letter_grade())


def start_run():
    """Ejecuta una demostración del programa."""
    student = Student("001", "Ana")
    student.add_grade(100)
    student.add_grade(50)
    student.check_honor()
    try:
        student.delete_grade(5)
    except IndexError:
        print("Error: no existe una calificación en esa posición.")
    student.report()

start_run()