__author__ = 'talhatekden'

import unittest
import Main.Modul1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        val=Main.Modul1.listsize([])
        self.assertEqual(val,0)


if __name__ == '__main__':
    unittest.main()
