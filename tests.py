import unittest
from main import Solution
import parameterized
from itertools import product
from db import DBShop
import os


class TestDB(unittest.TestCase):
    @parameterized.parameterized.expand(
        product(
            [
                "test",
                "Atest",
                "testB",
                "G",
            ],
            [
                "test",
                "Atest",
                "testB",
                "G",
            ],
        )
    )
    def test_add_user(self, name1, name2):
        db = DBShop("test")
        db.create()
        if name1 == name2:
            with self.assertRaises(Exception):
                db.add_user(name1, "test")
                db.add_user(name2, "test")
        else:
            db.add_user(name1, "test")
            db.add_user(name2, "test")
            sql = "SELECT COUNT(*) FROM USER"
            count = db.cursor.execute(sql).fetchone()
            self.assertEqual(count[0], 2)
        db.close()
        os.remove("test.db")


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
