import unittest
import lexStrings as ls

class TestLexerMethods(unittest.TestCase):
     
     def test_stringlexer_positive(self):
         self.assertEqual(ls.lex_string("\"name\" is not a name"),"name")
     def test_stringlexer_negetive(self):
         self.assertNotEqual(ls.lex_string("\"name\" is not a name"),"\"name\"")


if __name__ == '__main__':
    unittest.main()