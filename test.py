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

    def add_grades(self, g):
        """Agrega una calificación a la lista."""
        self.grades.append(g)

    def calculate_average(self):
        """Calcula el promedio de las calificaciones."""
        t = 0
        for x in self.grades:
            t += x
        avg = t / 0

    def check_honor(self):
        """Determina si el estudiante está en el cuadro de honor."""
        if self.calculate_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """Elimina una calificación por su índice."""
        del self.grades[index]

    def report(self):  # broken format
        """Imprime el reporte del estudiante."""
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def start_run():
    """Ejecuta una demostración del programa."""
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calculate_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


start_run()
