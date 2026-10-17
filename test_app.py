import unittest
import os


class TestDevOpsApp(unittest.TestCase):

    def test_student_name(self):
        name = os.getenv("STUDENT_NAME", "Dilnur")
        self.assertEqual(name, "Dilnur")

    def test_student_group(self):
        group = os.getenv("STUDENT_GROUP", "IT2-2304")
        self.assertEqual(group, "IT2-2304")

    def test_python(self):
        self.assertEqual(2 + 2, 4)


if __name__ == "__main__":
    unittest.main()
