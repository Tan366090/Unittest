
# gọi thư viện Unittest
import unittest
import time

# định nghĩa một lớp học sinh với các thuộc tính là tên, tuổi, và điểm trung bình của học sinh đó.
class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

# lớp danh sách học sinh.
class StudentList:
    # hàm khởi tạo danh sách sinh viên rỗng
    def __init__(self):
        self.students = []

    # hàm thêm học sinh vào danh sách
    def add_student(self, student):
        self.students.append(student)

    # hàm tính điểm trung bình GPA của các học sinh
    def get_average_gpa(self):
        # Kiểm tra xem danh sách học sinh có rỗng không
        if not self.students:
            return 0

        total_gpa = 0
        # Lặp qua từng học sinh trong danh sách
        for student in self.students:
            # Cộng điểm GPA của học sinh vào tổng điểm
            total_gpa += student.gpa

        # Tính điểm trung bình GPA
        average_gpa = total_gpa / len(self.students)

        # Trả về điểm trung bình GPA
        return average_gpa

class TestStudentList(unittest.TestCase):
    def setUp(self):
        print("Tạo môi trường cho kiểm thử...")
        self.student_list = StudentList()
        time.sleep(1)

    def tearDown(self):
        print("Dọn dẹp môi trường kiểm thử...\n")
        del self.student_list
        time.sleep(1)

    def test_add_student(self):
        print("\t\t Kiểm tra thêm học sinh vào danh sách...")
        time.sleep(1)
        student = Student("Nguyen van A", 20, 4.2)
        self.student_list.add_student(student)
        self.assertIn(student, self.student_list.students)
        print("\t\t Thêm học sinh hoàn tất!")
        time.sleep(1)


    def test_average_gpa_with_students(self):
        print("\t\t Kiểm tra điểm trung bình GPA cho danh sách có học sinh...")
        time.sleep(1)
        students = [
            Student("Tran van A", 21, 9.0),
            Student("Tran van B", 10, 8.7),
            Student("Tran van C", 22, 3.6)
        ]
        for student in students:
            self.student_list.add_student(student)
        self.assertEqual(self.student_list.get_average_gpa(), 7.1000000000000005)
        print("\t\t Kiểm tra điểm trung bình GPA cho danh sách có học sinh hoàn tất!")
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()