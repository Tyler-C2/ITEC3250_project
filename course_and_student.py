import statistics as stat

class Student():
    def __init__(self, student_id, grades):
        self.student_id = student_id
        self.grades = grades

class Course():
    def __init__(self):
        self.students=[]

    def create_student(self, lst):
        new_student = Student(lst[0],lst[1:])
        self.students.append(new_student)

    def student_avg(self, requested_id):
        for student in self.students:
            if student.student_id == requested_id:
                return round(stat.mean(student.grades), 2)

        return "Student not found"
        
    def course_avg(self):
        sum = 0

        for student in self.students:
            single_average = self.student_avg(student.student_id)
            sum += single_average

        return round(sum / len(self.students), 2)

    def course_median(self):
        temp_lst = []
        for student in self.students:
            temp_lst += student.grades

        return stat.median(temp_lst)

    def course_mode(self):
        temp_lst = []
        for student in self.students:
            temp_lst += student.grades
        
        return stat.mode(temp_lst)
