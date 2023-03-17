import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("""
         main: function void () {
                 a = readInteger();
                //b = readFloat();
                //c = readBoolean();
                //d = readString();
        }
        """, "abc,<EOF>", 101))
