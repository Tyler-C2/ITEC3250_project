# Test Cases:
#   1) CSV Parsing:
#       a) Accept a CSV string in the format "StudentID,Exam1Score,Exam2Score,Exam3Score,StudentID,..." and correctly parse it. Note: Every student must have all three exam scores provided and they must be in the range 0-100. SUPPORTS FUNCTIONAL REQUIREMENT #1.
#       b) Incorrect CSV shows an error message. SUPPORTS NON-FUNCTIONAL REQUIREMENT #1.
#   2) Correctly display each student’s scores for each of the three exams as well as their average of the three. SUPPORTS FUNCTIONAL REQUIREMENT #2 WITH AVERAGE; INDIVIDUAL SCORES IS ADDITIONAL FOR TESTING EARLY CODE.
#   3) For each of the three exams, correctly display the exam’s average score, median score, and mode. SUPPORTS FUNCTIONAL REQUIREMENT #3.

from course_and_student import *

if __name__ == "__main__":
    new_course = Course()

    test_data = [1452,89,75,64,2563,99,56,32,8546,85,75,68]
    id1_scores = [89, 75, 64]
    id2_scores = [99, 56, 32]
    id3_scores = [85, 75, 68]
    test_str = ','.join([str(i) for i in test_data])
    empty_test_str = test_str + ","
    multiple_test_str = test_str + ",40"
    oor_test_str = test_str + ",101"
    
    course_avg_answers = [91.0, 68.67, 54.67]
    course_median_answers = [89, 75, 64]
    course_mode_answers = [89, 75, 64]
    
    # for avg tests
    student_id_for_testing = [1452,2563,8546,5555,69421,3564]
    avg_answers = [76,62.33,76,"Student not found","Student not found","Student not found"]

    #def addInput(test_data):
    #    n = test_data
    #    for i in range(0,len(n),4):
    #        s_lst = [n[i],n[i+1],n[i+2],n[i+3]]
    #        new_course.create_student(s_lst)

    def test_student_avg(course_instance, ids, answers):
        for i in range(len(ids)):
            if course_instance.student_avg(ids[i]) != answers[i]:
                return False
        return True

    def test_course_avg(course_instance, answer):
        assert course_instance.course_avg() == answer

    def test_median(course_instance, answer):
       assert course_instance.course_median() == answer

    def test_mode(course_instance, answer):
       assert course_instance.course_mode() == answer
    
    def test_case1():
        c = Course()
        ret_good = "Student information processed."
        if c.parse_csv(test_str) == ret_good and c.parse_csv(empty_test_str) != ret_good and c.parse_csv(multiple_test_str) != ret_good and c.parse_csv(oor_test_str) != ret_good:
            print("Test Case 1 (Correctly parse CSV): Pass")
        else:
            print("Test Case 1 (Correctly parse CSV): FAIL")
            
    def test_case2():
        c = Course()
        ret_good = "Student information processed."
        if c.parse_csv(test_str) == ret_good:
            # csv parsed right
            if not test_student_avg(c, student_id_for_testing, avg_answers):
                # student avgs are incorrect
                print("Test Case 2 (Student Scores): FAIL")
            else:
                # student avgs are correct
                
                # check students scores
                students = []
                for i in range(len(c.students)):
                    students.append(c.students[i].student_id)
                    for k in range(len(c.students[i].grades)):
                        students.append(c.students[i].grades[k])
                if students == test_data:
                    print("Test Case 2 (Student Scores): Pass")
                else:
                    print("Test Case 2 (Student Scores): FAIL")
        else:
            # csv parse fail
            print("Test Case 2 (Student Scores): FAIL")
            
    def test_case3():
        c = Course()
        ret_good = "Student information processed."
        if c.parse_csv(test_str) == ret_good:
            test_course_avg(c, course_avg_answers)
            test_median(c, course_median_answers)
            test_mode(c, course_mode_answers)
            print("Test Case 3 (Avg, Median, Mode): Pass")
        else:
            print("Test Case 3 (Avg, Median, Mode): FAIL")

    # test execution
    #addInput(test_data) 
    #test_course_avg(new_course, [91.0, 68.67, 54.67])
    #test_median(new_course, [89, 75, 64])
    #test_mode(new_course, [89, 75, 64])
    test_case1()
    test_case2()
    test_case3()
