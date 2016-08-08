import unittest

class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_integer_equal(self):
        self.assertEqual(2+2,1+3)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_splitfun(self):
        s = "hello world common"
        self.assertEqual(s.split(),['hello','world','common'])
        with self.assertRaises(TypeError):
            s.split(2)

suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethod)
unittest.TextTestRunner(verbosity=2).run(suite)
