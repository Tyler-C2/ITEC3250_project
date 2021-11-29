# Test Cases:
#   1) CSV Parsing:
#       a) Accept a CSV string in the format "StudentID,Exam1Score,Exam2Score,Exam3Score,StudentID,..." and correctly parse it. Note: Every student must have all three exam scores provided and they must be in the range 0-100. SUPPORTS FUNCTIONAL REQUIREMENT #1.
#       b) Incorrect CSV shows an error message. SUPPORTS NON-FUNCTIONAL REQUIREMENT #1.
#   2) Correctly display each student’s scores for each of the three exams as well as their average of the three. SUPPORTS FUNCTIONAL REQUIREMENT #2 WITH AVERAGE; INDIVIDUAL SCORES IS ADDITIONAL FOR TESTING EARLY CODE.
#   3) For each of the three exams, correctly display the exam’s average score, median score, and score range (minimum-maximum). SUPPORTS FUNCTIONAL REQUIREMENT #3.

if __name__ == "__main__":
    
