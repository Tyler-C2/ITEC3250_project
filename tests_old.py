from course_and_student import *

if __name__ == "__main__":
    new_course = Course()

    test_data = [1452,89,75,64,2563,99,56,32,8546,85,75,68]
    
    # for avg tests
    student_id_for_testing = [1452,2563,8546,5555,69421,3564]
    avg_answers = [76,62.33,76,"Student not found","Student not found","Student not found"]

    def addInput(test_data):
        n = test_data
        for i in range(0,len(n),4):
            s_lst = [n[i],n[i+1],n[i+2],n[i+3]]
            new_course.create_student(s_lst)

    def test_student_avg(course_instance, ids, answers):
        for i in range(len(ids)):
            assert course_instance.student_avg(ids[i]) == answers[i]

    def test_course_avg(course_instance, answer):
        assert course_instance.course_avg() == answer

    def test_median(course_instance, answer):
       assert course_instance.course_median() == answer        

    def test_mode(course_instance, answer):
       assert course_instance.course_mode() == answer        

    # test execution
    addInput(test_data) 
    test_student_avg(new_course, student_id_for_testing, avg_answers)
    test_course_avg(new_course, [91.0, 68.67, 54.67])
    test_median(new_course, [89, 75, 64])
    test_mode(new_course, [89, 75, 64])
