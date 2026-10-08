"""Módulo para gestionar estudiantes y sus calificaciones."""

class Student:
    """Estudiante con su ID, nombre y lista de calificaciones."""

    def __init__(self, student_id, name):
        """Crea el estudiante, el ID y el nombre no pueden estar vacíos."""
        if not str(student_id).strip():
            raise ValueError("El ID no puede estar vacío.")
        if not str(name).strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.student_id = str(student_id).strip()
        self.name = str(name).strip()
        self.grades = []

    def add_grade(self, grade):
        """Agrega una nota numérica entre 0 y 100."""
        if not isinstance(grade, (int, float)):
            raise ValueError(f"La nota '{grade}' no es un número.")
        if grade < 0 or grade > 100:
            raise ValueError(f"La nota {grade} debe estar entre 0 y 100.")
        self.grades.append(float(grade))

    def calculate_average(self):
        """Devuelve el promedio de las notas (0 si no hay notas)."""
        if len(self.grades) == 0:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Devuelve la letra según el promedio."""
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

    def get_status(self):
        """Devuelve 'Passed' o 'Failed'."""
        if self.calculate_average() >= 60:
            return "Passed"
        return "Failed"

    def is_honor_roll(self):
        """Devuelve True si el promedio es 90 o más."""
        return self.calculate_average() >= 90

    def remove_grade_by_index(self, index):
        """Elimina la nota en la posición indicada (desde 0)."""
        if index < 0 or index >= len(self.grades):
            raise IndexError(f"No hay ninguna nota en la posición {index}.")
        self.grades.pop(index)

    def remove_grade_by_value(self, value):
        """Elimina la primera nota que tenga ese valor."""
        if value not in self.grades:
            raise ValueError(f"La nota {value} no existe.")
        self.grades.remove(value)

    def report(self):
        """Imprime el resumen del estudiante."""
        print("-" * 30)
        print(f"Student ID:    {self.student_id}")
        print(f"Student Name:  {self.name}")
        print(f"Grades Count:  {len(self.grades)}")
        print(f"Average Grade: {self.calculate_average():.2f}")
        print(f"Letter Grade:  {self.get_letter_grade()}")
        print(f"Status:        {self.get_status()}")
        print(f"Honor Roll:    {self.is_honor_roll()}")
        print("-" * 30)

def start_run():
    """Prueba el programa con datos válidos e inválidos."""
    try:
        student = Student("001", "Ana")
    except ValueError as error:
        print("Error:", error)
        return

    for grade in (95.0, 72.5, "Fifty", 150):
        try:
            student.add_grade(grade)
        except ValueError as error:
            print("Error:", error)

    try:
        student.remove_grade_by_index(5)
    except IndexError as error:
        print("Error:", error)

    try:
        student.remove_grade_by_value(10)
    except ValueError as error:
        print("Error:", error)

    student.remove_grade_by_index(1)
    student.report()

    try:
        Student("", "Luis")
    except ValueError as error:
        print("Error:", error)

start_run()
