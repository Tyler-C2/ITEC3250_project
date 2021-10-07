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
        exam_sums = [0,0,0]
        avg_lst = []

        for student in self.students:
            for i in range(len(student.grades)):
                exam_sums[i] += student.grades[i]

        for sum in exam_sums:
            avg_lst.append(round(sum / len(self.students), 2))

        return avg_lst

    def course_median(self):
        exam_grouping = [[],[],[]]
        medians = []
        for student in self.students:
            for i in range(len(student.grades)):
                exam_grouping[i].append(student.grades[i])

        for group in exam_grouping:
            medians.append(stat.median(group))
            
        return medians

    def course_mode(self):
        exam_grouping = [[],[],[]]
        modes = []

        for student in self.students:
            for i in range(len(student.grades)):
                exam_grouping[i].append(student.grades[i])

        for group in exam_grouping:
            modes.append(stat.mode(group))
        
        return modes
