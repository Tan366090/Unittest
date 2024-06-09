import unittest

# Import các lớp test case từ các file tương ứng
from Unittest.Testcase.test_sum import TestSum
from Unittest.Testclass.test_ClassSV import TestStudentList
from Unittest.TestFunctions.test_Functions import TestFunctions

# Tạo một bộ test
suite = unittest.TestSuite()

# Sử dụng unittest.TestLoader.loadTestsFromTestCase() thay thế cho unittest.makeSuite()
loader = unittest.TestLoader()

# Thêm các test case vào bộ test
suite.addTest(loader.loadTestsFromTestCase(TestSum))
suite.addTest(loader.loadTestsFromTestCase(TestStudentList))
suite.addTest(loader.loadTestsFromTestCase(TestFunctions))

# Tạo một đối tượng để chạy test
runner = unittest.TextTestRunner()

# Chạy bộ test
result = runner.run(suite)