import unittest
import time

def is_prime(n):
  """Kiểm tra số nguyên tố."""
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def is_perfect_square(n):
  """Kiểm tra số chính phương."""
  return int(n ** 0.5) ** 2 == n

def is_perfect_number(n):
  """Kiểm tra số hoàn hảo."""
  sum_divisors = 1
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      sum_divisors += i + n // i
  return sum_divisors == n


class TestFunctions(unittest.TestCase):
  def test_is_prime(self):
    print("Test số NGUYÊN TỐ,..")
    time.sleep(1)
    self.assertFalse(is_prime(20))
    self.assertTrue(is_prime(7))
    print("Đã Test xong số NGUYÊN TỐ,...\n\n")
    time.sleep(2)

  def test_is_perfect_square(self):
    print("Test số CHÍNH PHƯƠNG,...")
    time.sleep(1)
    self.assertTrue(is_perfect_square(25))
    self.assertFalse(is_perfect_square(5))
    print("Đã Test xong số CHÍNH PHƯƠNG,...\n\n")
    time.sleep(2)


  def test_is_perfect_number(self):
    print("Test số HOÀN HẢO,...")
    time.sleep(1)
    self.assertTrue(is_perfect_number(6))
    self.assertFalse(is_perfect_number(2))
    print("Đã Test xong số HOÀN HẢO,...\n\n")
    time.sleep(2)

if __name__ == '__main__':
  unittest.main()
