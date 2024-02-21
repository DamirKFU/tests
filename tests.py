import unittest
from main import Solution


class TestStringMethods(unittest.TestCase):
    def test_rims_fucntion(self):
        tests = [
            (4444, "MMMMCDXLIV"),
            (4, "IV"),
            (9, "IX"),
            (40, "XL"),
            (90, "XC"),
            (400, "CD"),
            (900, "CM"),
            (237, "CCXXXVII"),
        ]
        for value, expected in tests:
            with self.subTest(value=value):
                self.assertEqual(
                    Solution.romanToInt(value),
                    expected,
                    msg="тест на риские цифры не пройден",
                )


if __name__ == "__main__":
    unittest.main()
