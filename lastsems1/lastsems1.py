#num1
# import unittest
#
#
# def factorize(number):
#     if not isinstance(number, int):
#         raise TypeError("Input must be an integer")
#     if number <= 0:
#         raise ValueError("Input must be positive")
#
#     factors = []
#     d = 2
#     temp = number
#     while d * d <= temp:
#         while temp % d == 0:
#             factors.append(d)
#             temp //= d
#         d += 1
#     if temp > 1:
#         factors.append(temp)
#     return factors
#
#
# class TestPrimeFactors(unittest.TestCase):
#     def test_simple_cases(self):
#         self.assertEqual(factorize(10), [2, 5])
#         self.assertEqual(factorize(12), [2, 2, 3])
#         self.assertEqual(factorize(100), [2, 2, 5, 5])
#
#     def test_primes(self):
#         self.assertEqual(factorize(13), [13])
#         self.assertEqual(factorize(2), [2])
#
#     def test_errors(self):
#         with self.assertRaises(TypeError):
#             factorize("100")
#
#         with self.assertRaises(ValueError):
#             factorize(-10)
#
#
# if __name__ == '__main__':
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)

# num2
# import unittest
#
#
# def get_lsm_coeffs(x, y):
#
#     if len(x) != len(y):
#         raise ValueError("Arrays must have equal length")
#     if len(x) < 2:
#         raise ValueError("At least 2 points required")
#
#     n = len(x)
#     sum_x = sum(x)
#     sum_y = sum(y)
#     sum_xy = sum(xi * yi for xi, yi in zip(x, y))
#     sum_x_sq = sum(xi ** 2 for xi in x)
#
#     denominator = n * sum_x_sq - sum_x ** 2
#
#     if denominator == 0:
#         raise ValueError("Vertical line detected (denominator is zero)")
#
#     k = (n * sum_xy - sum_x * sum_y) / denominator
#     b = (sum_y - k * sum_x) / n
#     return k, b
#
#
# class TestLSM(unittest.TestCase):
#     def test_ideal_line(self):
#         x = [0, 1, 2, 3]
#         y = [3, 5, 7, 9]
#         k, b = get_lsm_coeffs(x, y)
#         self.assertAlmostEqual(k, 2.0)
#         self.assertAlmostEqual(b, 3.0)
#
#     def test_horizontal_line(self):
#         x = [1, 2, 3]
#         y = [5, 5, 5]
#         k, b = get_lsm_coeffs(x, y)
#         self.assertAlmostEqual(k, 0.0)
#         self.assertAlmostEqual(b, 5.0)
#
#     def test_validation(self):
#         with self.assertRaises(ValueError):
#             get_lsm_coeffs([1, 2, 3], [1, 2])
#
#         with self.assertRaises(ValueError):
#             get_lsm_coeffs([1], [1])
#
#
# if __name__ == '__main__':
#     unittest.main(argv=['ignored'], exit=False)

# num3
# import unittest
# import random
#
#
# def quick_sort(arr):
#     if not isinstance(arr, list):
#         raise TypeError(f"Expected list, got {type(arr)}")
#
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#
#     return quick_sort(left) + middle + quick_sort(right)
#
#
# class TestQuickSort(unittest.TestCase):
#     def test_standard_case(self):
#         data = [3, 6, 8, 10, 1, 2, 1]
#         expected = sorted(data)
#         self.assertEqual(quick_sort(data), expected,
#                          "Should be sorted ascending")
#
#     def test_empty_and_single(self):
#         self.assertEqual(quick_sort([]), [])
#         self.assertEqual(quick_sort([5]), [5])
#
#     def test_negative_numbers(self):
#         data = [-1, -5, 0, 10, 2]
#         self.assertEqual(quick_sort(data), [-5, -1, 0, 2, 10])
#
#     def test_duplicates(self):
#         self.assertEqual(quick_sort([2, 2, 2]), [2, 2, 2])
#
#     def test_input_validation(self):
#         with self.assertRaises(TypeError):
#             quick_sort("not a list")
#
#
# if __name__ == '__main__':
#     unittest.main(argv=['ignored'], exit=False)

# num4
# import unittest
#
#
# def decrypt_caesar(ciphertext, shift):
#     if not isinstance(ciphertext, str):
#         raise TypeError("Ciphertext must be a string")
#     if not isinstance(shift, int):
#         raise TypeError("Shift must be an integer")
#
#     result = []
#     for char in ciphertext:
#         if char.isalpha():
#             base = ord('A') if char.isupper() else ord('a')
#             decrypted_char = chr((ord(char) - shift - base) % 26 + base)
#             result.append(decrypted_char)
#         else:
#             result.append(char)
#     return "".join(result)
#
#
# class TestCaesarCipher(unittest.TestCase):
#
#     def test_basic_decryption(self):
#         self.assertEqual(decrypt_caesar("Ifmmp", 1), "Hello")
#
#     def test_sentence_with_punctuation(self):
#         self.assertEqual(decrypt_caesar("Khoor, Zruog!", 3), "Hello, World!")
#
#     def test_wrapping(self):
#         self.assertEqual(decrypt_caesar("A", 1), "Z")
#         self.assertEqual(decrypt_caesar("abc", 3), "xyz")
#
#     def test_large_shift(self):
#         self.assertEqual(decrypt_caesar("Ifmmp", 27), "Hello")
#
#     def test_validation(self):
#         with self.assertRaises(TypeError):
#             decrypt_caesar(123, 5)
#
#
# if __name__ == '__main__':
#     unittest.main(argv=['ignored'], exit=False)
