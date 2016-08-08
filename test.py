import unittest

class TestStringMethod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('FOO'.isupper())

    def test_split(self):
        s= 'hello world'
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            s.split(2)

suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethod)
unittest.TextTestRunner(verbosity=2).run(suite)