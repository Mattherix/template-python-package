from unittest import main, TestCase
from .. import add


class Test(TestCase):
    def test_add(self):
        # Positive & Negative number
        self.assertAlmostEqual(add(10, 100), 110)
        self.assertAlmostEqual(add(-20, 99), 79)
        self.assertAlmostEqual(add(-10, -100), -110)

        # Relative number
        self.assertAlmostEqual(add(0.1, -0.5), -0.4)
        self.assertAlmostEqual(add(-0.1, 100), 99.9)

        # Not equal
        self.assertNotAlmostEqual(add(1, 1), 3)


if __name__ == '__main__':
    main()

