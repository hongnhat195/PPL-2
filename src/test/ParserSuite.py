import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_short_vardecl(self):
        """Test short variable declaration"""
        input = """ main: function void () {
                 a = readInteger();
                //b = readFloat();
                //c = readBoolean();
                //d = readString();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
