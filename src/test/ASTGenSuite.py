import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    #     def test_short_vardecl(self):
    #         input = """x: integer;"""
    #         expect = str(Program([VarDecl("x", IntegerType())]))
    #         self.assertTrue(TestAST.test(input, expect, 300))

    #     def test_full_vardecl(self):
    #         input = """x, y, z: integer = 1, 2, 3;"""
    #         expect = """Program([
    # 	VarDecl(x, IntegerType, IntegerLit(1))
    # 	VarDecl(y, IntegerType, IntegerLit(2))
    # 	VarDecl(z, IntegerType, IntegerLit(3))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 301))

    #     def test_vardecls(self):
    #         input = """x, y, z: integer = 1, 2, 3;
    #         a, b: float;"""
    #         expect = """Program([
    # 	VarDecl(x, IntegerType, IntegerLit(1))
    # 	VarDecl(y, IntegerType, IntegerLit(2))
    # 	VarDecl(z, IntegerType, IntegerLit(3))
    # 	VarDecl(b, FloatType)
    # 	VarDecl(a, FloatType)
    # """
    #         self.assertTrue(TestAST.test(input, expect, 302))

    #     def test_simple_program(self):
    #         """Simple program"""
    #         input = """main: function void () {
    #         }"""
    #         expect = """Program([
    # 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            myPets : array[5, 6] of string ;
            printInteger(4);
            x: integer = 5;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        """Test 305"""
        input = """
        x : integer = 65;
        fact : function integer (n : integer, m: float) {
        if (n == 0) return 1;
         else return n*fact(n-1);
        return 3;
        }
       inc : function void (out n: integer, delta: integer){
        n = n + delta ;
        }
        main : function void () {
        delta : integer = fact(3);
        inc(x, delta);
        printInt(x);
        }

        """
        expect = """"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        "Test 306"
        input = """main: function void () {}"""
        expect = """"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        "Test 307"
        input = """
        foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

        main: function void () {
        printInteger(4);
        } """
        expect = """"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        """Test 308"""
        input = """main: function void () {
                do {
                    x, y, z: integer = 1, 2, 3;
                    if (a == 10) continue;
                    a = a - 1; 
                    printInteger(a);
                    z = a[x+5, y+5, z+5];
                }
                while(a > 0);
            } """
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 308))
