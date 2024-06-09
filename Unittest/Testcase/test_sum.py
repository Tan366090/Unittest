import unittest
import time
def tinh_tong(a, b):
  return a + b


class TestSum(unittest.TestCase):
  def test_tinh_tong_so_nguyen(self):
    Ketqua = tinh_tong(2, 3)
    self.assertEqual(Ketqua, 5)
    self.assertNotEqual(Ketqua, 4)
    self.assertTrue(Ketqua > 2)
    self.assertFalse(Ketqua > 8)
    print("\n\nĐã test xong hàm tính tổng...\n")
    time.sleep(1.5)
#   ...và một số assert methods khác
if __name__ == '__main__':
  unittest.main()



# import unittest
# import time
# from parameterized import parameterized
#
# def tinh_tong(a, b):
#   return a + b
#
# class TestSum(unittest.TestCase):
#   @parameterized.expand([
#     (2, 3, 5),
#     (-1, 4, 3),
#     (5, -5, 0),
#   ])
#   def test_tinh_tong_so_nguyen(self, a, b, expected_result):
#     Ketqua = tinh_tong(a, b)
#     self.assertEqual(Ketqua, expected_result)
#     self.assertNotEqual(Ketqua, expected_result - 1)
#     print("\n\nĐã test xong hàm tính tổng...\n")
#     time.sleep(1.5)
#
# if __name__ == '__main__':
#   unittest.main()