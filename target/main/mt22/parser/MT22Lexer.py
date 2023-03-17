# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0263\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!")
        buf.write("\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(")
        buf.write("\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3")
        buf.write(";\3;\7;\u01c1\n;\f;\16;\u01c4\13;\3<\3<\3<\7<\u01c9\n")
        buf.write("<\f<\16<\u01cc\13<\3<\5<\u01cf\n<\3<\3<\6<\u01d3\n<\r")
        buf.write("<\16<\u01d4\3<\6<\u01d8\n<\r<\16<\u01d9\3<\3<\3<\3<\3")
        buf.write("<\5<\u01e1\n<\3<\3<\3=\3=\5=\u01e7\n=\3=\6=\u01ea\n=\r")
        buf.write("=\16=\u01eb\3>\3>\7>\u01f0\n>\f>\16>\u01f3\13>\3>\7>\u01f6")
        buf.write("\n>\f>\16>\u01f9\13>\3>\6>\u01fc\n>\r>\16>\u01fd\7>\u0200")
        buf.write("\n>\f>\16>\u0203\13>\3>\3>\5>\u0207\n>\3?\3?\7?\u020b")
        buf.write("\n?\f?\16?\u020e\13?\3?\3?\3?\3@\3@\3@\5@\u0216\n@\3A")
        buf.write("\3A\3A\3B\3B\3B\3C\6C\u021f\nC\rC\16C\u0220\3C\3C\3D\6")
        buf.write("D\u0226\nD\rD\16D\u0227\3D\3D\3D\3E\3E\3E\3E\7E\u0231")
        buf.write("\nE\fE\16E\u0234\13E\3E\3E\3E\3E\3E\3F\3F\3F\3F\7F\u023f")
        buf.write("\nF\fF\16F\u0242\13F\3F\3F\3G\3G\7G\u0248\nG\fG\16G\u024b")
        buf.write("\13G\3G\5G\u024e\nG\3G\3G\3H\3H\3H\5H\u0255\nH\3I\3I\7")
        buf.write("I\u0259\nI\fI\16I\u025c\13I\3I\3I\3I\3J\3J\3J\3\u0232")
        buf.write("\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y\2{>}?\177\2\u0081\2\u0083\2\u0085@\u0087A\u0089")
        buf.write("B\u008bC\u008dD\u008f\2\u0091E\u0093F\3\2\20\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\3\2\63;\5\2")
        buf.write("\f\f$$^^\t\2))^^ddhhppttvv\5\2\13\f\17\17\"\"\4\2\f\f")
        buf.write("\"\"\4\2\f\f\17\17\3\3\f\f\n\2$$))^^ddhhppttvv\3\2^^\2")
        buf.write("\u0276\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2{\3\2")
        buf.write("\2\2\2}\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u009a\3\2\2\2\7\u00a0")
        buf.write("\3\2\2\2\t\u00a8\3\2\2\2\13\u00ab\3\2\2\2\r\u00b0\3\2")
        buf.write("\2\2\17\u00b6\3\2\2\2\21\u00bc\3\2\2\2\23\u00c0\3\2\2")
        buf.write("\2\25\u00c3\3\2\2\2\27\u00cb\3\2\2\2\31\u00d2\3\2\2\2")
        buf.write("\33\u00d9\3\2\2\2\35\u00de\3\2\2\2\37\u00e4\3\2\2\2!\u00e9")
        buf.write("\3\2\2\2#\u00ed\3\2\2\2%\u00f6\3\2\2\2\'\u00f9\3\2\2\2")
        buf.write(")\u0101\3\2\2\2+\u0107\3\2\2\2-\u0110\3\2\2\2/\u011c\3")
        buf.write("\2\2\2\61\u0129\3\2\2\2\63\u0133\3\2\2\2\65\u013e\3\2")
        buf.write("\2\2\67\u014a\3\2\2\29\u0157\3\2\2\2;\u0162\3\2\2\2=\u016e")
        buf.write("\3\2\2\2?\u0174\3\2\2\2A\u0183\3\2\2\2C\u0185\3\2\2\2")
        buf.write("E\u0187\3\2\2\2G\u0189\3\2\2\2I\u018b\3\2\2\2K\u018d\3")
        buf.write("\2\2\2M\u018f\3\2\2\2O\u0192\3\2\2\2Q\u0195\3\2\2\2S\u0198")
        buf.write("\3\2\2\2U\u019b\3\2\2\2W\u019d\3\2\2\2Y\u01a0\3\2\2\2")
        buf.write("[\u01a2\3\2\2\2]\u01a5\3\2\2\2_\u01a8\3\2\2\2a\u01aa\3")
        buf.write("\2\2\2c\u01ac\3\2\2\2e\u01ae\3\2\2\2g\u01b0\3\2\2\2i\u01b2")
        buf.write("\3\2\2\2k\u01b4\3\2\2\2m\u01b6\3\2\2\2o\u01b8\3\2\2\2")
        buf.write("q\u01ba\3\2\2\2s\u01bc\3\2\2\2u\u01be\3\2\2\2w\u01e0\3")
        buf.write("\2\2\2y\u01e4\3\2\2\2{\u0206\3\2\2\2}\u0208\3\2\2\2\177")
        buf.write("\u0215\3\2\2\2\u0081\u0217\3\2\2\2\u0083\u021a\3\2\2\2")
        buf.write("\u0085\u021e\3\2\2\2\u0087\u0225\3\2\2\2\u0089\u022c\3")
        buf.write("\2\2\2\u008b\u023a\3\2\2\2\u008d\u0245\3\2\2\2\u008f\u0254")
        buf.write("\3\2\2\2\u0091\u0256\3\2\2\2\u0093\u0260\3\2\2\2\u0095")
        buf.write("\u0096\7c\2\2\u0096\u0097\7w\2\2\u0097\u0098\7v\2\2\u0098")
        buf.write("\u0099\7q\2\2\u0099\4\3\2\2\2\u009a\u009b\7d\2\2\u009b")
        buf.write("\u009c\7t\2\2\u009c\u009d\7g\2\2\u009d\u009e\7c\2\2\u009e")
        buf.write("\u009f\7m\2\2\u009f\6\3\2\2\2\u00a0\u00a1\7d\2\2\u00a1")
        buf.write("\u00a2\7q\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4\7n\2\2\u00a4")
        buf.write("\u00a5\7g\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7\7p\2\2\u00a7")
        buf.write("\b\3\2\2\2\u00a8\u00a9\7f\2\2\u00a9\u00aa\7q\2\2\u00aa")
        buf.write("\n\3\2\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7n\2\2\u00ad")
        buf.write("\u00ae\7u\2\2\u00ae\u00af\7g\2\2\u00af\f\3\2\2\2\u00b0")
        buf.write("\u00b1\7h\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3\7n\2\2\u00b3")
        buf.write("\u00b4\7u\2\2\u00b4\u00b5\7g\2\2\u00b5\16\3\2\2\2\u00b6")
        buf.write("\u00b7\7h\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7q\2\2\u00b9")
        buf.write("\u00ba\7c\2\2\u00ba\u00bb\7v\2\2\u00bb\20\3\2\2\2\u00bc")
        buf.write("\u00bd\7h\2\2\u00bd\u00be\7q\2\2\u00be\u00bf\7t\2\2\u00bf")
        buf.write("\22\3\2\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2\7h\2\2\u00c2")
        buf.write("\24\3\2\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7p\2\2\u00c5")
        buf.write("\u00c6\7v\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7i\2\2\u00c8")
        buf.write("\u00c9\7g\2\2\u00c9\u00ca\7t\2\2\u00ca\26\3\2\2\2\u00cb")
        buf.write("\u00cc\7t\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7v\2\2\u00ce")
        buf.write("\u00cf\7w\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1\7p\2\2\u00d1")
        buf.write("\30\3\2\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4\7v\2\2\u00d4")
        buf.write("\u00d5\7t\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7p\2\2\u00d7")
        buf.write("\u00d8\7i\2\2\u00d8\32\3\2\2\2\u00d9\u00da\7v\2\2\u00da")
        buf.write("\u00db\7t\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd\7g\2\2\u00dd")
        buf.write("\34\3\2\2\2\u00de\u00df\7y\2\2\u00df\u00e0\7j\2\2\u00e0")
        buf.write("\u00e1\7k\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3\7g\2\2\u00e3")
        buf.write("\36\3\2\2\2\u00e4\u00e5\7x\2\2\u00e5\u00e6\7q\2\2\u00e6")
        buf.write("\u00e7\7k\2\2\u00e7\u00e8\7f\2\2\u00e8 \3\2\2\2\u00e9")
        buf.write("\u00ea\7q\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec\7v\2\2\u00ec")
        buf.write("\"\3\2\2\2\u00ed\u00ee\7e\2\2\u00ee\u00ef\7q\2\2\u00ef")
        buf.write("\u00f0\7p\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7k\2\2\u00f2")
        buf.write("\u00f3\7p\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5\7g\2\2\u00f5")
        buf.write("$\3\2\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7h\2\2\u00f8")
        buf.write("&\3\2\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb\7p\2\2\u00fb")
        buf.write("\u00fc\7j\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7t\2\2\u00fe")
        buf.write("\u00ff\7k\2\2\u00ff\u0100\7v\2\2\u0100(\3\2\2\2\u0101")
        buf.write("\u0102\7c\2\2\u0102\u0103\7t\2\2\u0103\u0104\7t\2\2\u0104")
        buf.write("\u0105\7c\2\2\u0105\u0106\7{\2\2\u0106*\3\2\2\2\u0107")
        buf.write("\u0108\7h\2\2\u0108\u0109\7w\2\2\u0109\u010a\7p\2\2\u010a")
        buf.write("\u010b\7e\2\2\u010b\u010c\7v\2\2\u010c\u010d\7k\2\2\u010d")
        buf.write("\u010e\7q\2\2\u010e\u010f\7p\2\2\u010f,\3\2\2\2\u0110")
        buf.write("\u0111\7t\2\2\u0111\u0112\7g\2\2\u0112\u0113\7c\2\2\u0113")
        buf.write("\u0114\7f\2\2\u0114\u0115\7K\2\2\u0115\u0116\7p\2\2\u0116")
        buf.write("\u0117\7v\2\2\u0117\u0118\7g\2\2\u0118\u0119\7i\2\2\u0119")
        buf.write("\u011a\7g\2\2\u011a\u011b\7t\2\2\u011b.\3\2\2\2\u011c")
        buf.write("\u011d\7r\2\2\u011d\u011e\7t\2\2\u011e\u011f\7k\2\2\u011f")
        buf.write("\u0120\7p\2\2\u0120\u0121\7v\2\2\u0121\u0122\7K\2\2\u0122")
        buf.write("\u0123\7p\2\2\u0123\u0124\7v\2\2\u0124\u0125\7g\2\2\u0125")
        buf.write("\u0126\7i\2\2\u0126\u0127\7g\2\2\u0127\u0128\7t\2\2\u0128")
        buf.write("\60\3\2\2\2\u0129\u012a\7t\2\2\u012a\u012b\7g\2\2\u012b")
        buf.write("\u012c\7c\2\2\u012c\u012d\7f\2\2\u012d\u012e\7H\2\2\u012e")
        buf.write("\u012f\7n\2\2\u012f\u0130\7q\2\2\u0130\u0131\7c\2\2\u0131")
        buf.write("\u0132\7v\2\2\u0132\62\3\2\2\2\u0133\u0134\7y\2\2\u0134")
        buf.write("\u0135\7t\2\2\u0135\u0136\7k\2\2\u0136\u0137\7v\2\2\u0137")
        buf.write("\u0138\7g\2\2\u0138\u0139\7H\2\2\u0139\u013a\7n\2\2\u013a")
        buf.write("\u013b\7q\2\2\u013b\u013c\7c\2\2\u013c\u013d\7v\2\2\u013d")
        buf.write("\64\3\2\2\2\u013e\u013f\7t\2\2\u013f\u0140\7g\2\2\u0140")
        buf.write("\u0141\7c\2\2\u0141\u0142\7f\2\2\u0142\u0143\7D\2\2\u0143")
        buf.write("\u0144\7q\2\2\u0144\u0145\7q\2\2\u0145\u0146\7n\2\2\u0146")
        buf.write("\u0147\7g\2\2\u0147\u0148\7c\2\2\u0148\u0149\7p\2\2\u0149")
        buf.write("\66\3\2\2\2\u014a\u014b\7r\2\2\u014b\u014c\7t\2\2\u014c")
        buf.write("\u014d\7k\2\2\u014d\u014e\7p\2\2\u014e\u014f\7v\2\2\u014f")
        buf.write("\u0150\7D\2\2\u0150\u0151\7q\2\2\u0151\u0152\7q\2\2\u0152")
        buf.write("\u0153\7n\2\2\u0153\u0154\7g\2\2\u0154\u0155\7c\2\2\u0155")
        buf.write("\u0156\7p\2\2\u01568\3\2\2\2\u0157\u0158\7t\2\2\u0158")
        buf.write("\u0159\7g\2\2\u0159\u015a\7c\2\2\u015a\u015b\7f\2\2\u015b")
        buf.write("\u015c\7U\2\2\u015c\u015d\7v\2\2\u015d\u015e\7t\2\2\u015e")
        buf.write("\u015f\7k\2\2\u015f\u0160\7p\2\2\u0160\u0161\7i\2\2\u0161")
        buf.write(":\3\2\2\2\u0162\u0163\7r\2\2\u0163\u0164\7t\2\2\u0164")
        buf.write("\u0165\7k\2\2\u0165\u0166\7p\2\2\u0166\u0167\7v\2\2\u0167")
        buf.write("\u0168\7U\2\2\u0168\u0169\7v\2\2\u0169\u016a\7t\2\2\u016a")
        buf.write("\u016b\7k\2\2\u016b\u016c\7p\2\2\u016c\u016d\7i\2\2\u016d")
        buf.write("<\3\2\2\2\u016e\u016f\7u\2\2\u016f\u0170\7w\2\2\u0170")
        buf.write("\u0171\7r\2\2\u0171\u0172\7g\2\2\u0172\u0173\7t\2\2\u0173")
        buf.write(">\3\2\2\2\u0174\u0175\7r\2\2\u0175\u0176\7t\2\2\u0176")
        buf.write("\u0177\7g\2\2\u0177\u0178\7x\2\2\u0178\u0179\7g\2\2\u0179")
        buf.write("\u017a\7p\2\2\u017a\u017b\7v\2\2\u017b\u017c\7F\2\2\u017c")
        buf.write("\u017d\7g\2\2\u017d\u017e\7h\2\2\u017e\u017f\7c\2\2\u017f")
        buf.write("\u0180\7w\2\2\u0180\u0181\7n\2\2\u0181\u0182\7v\2\2\u0182")
        buf.write("@\3\2\2\2\u0183\u0184\7-\2\2\u0184B\3\2\2\2\u0185\u0186")
        buf.write("\7/\2\2\u0186D\3\2\2\2\u0187\u0188\7,\2\2\u0188F\3\2\2")
        buf.write("\2\u0189\u018a\7\61\2\2\u018aH\3\2\2\2\u018b\u018c\7\'")
        buf.write("\2\2\u018cJ\3\2\2\2\u018d\u018e\7#\2\2\u018eL\3\2\2\2")
        buf.write("\u018f\u0190\7(\2\2\u0190\u0191\7(\2\2\u0191N\3\2\2\2")
        buf.write("\u0192\u0193\7~\2\2\u0193\u0194\7~\2\2\u0194P\3\2\2\2")
        buf.write("\u0195\u0196\7?\2\2\u0196\u0197\7?\2\2\u0197R\3\2\2\2")
        buf.write("\u0198\u0199\7#\2\2\u0199\u019a\7?\2\2\u019aT\3\2\2\2")
        buf.write("\u019b\u019c\7>\2\2\u019cV\3\2\2\2\u019d\u019e\7>\2\2")
        buf.write("\u019e\u019f\7?\2\2\u019fX\3\2\2\2\u01a0\u01a1\7@\2\2")
        buf.write("\u01a1Z\3\2\2\2\u01a2\u01a3\7@\2\2\u01a3\u01a4\7?\2\2")
        buf.write("\u01a4\\\3\2\2\2\u01a5\u01a6\7<\2\2\u01a6\u01a7\7<\2\2")
        buf.write("\u01a7^\3\2\2\2\u01a8\u01a9\7?\2\2\u01a9`\3\2\2\2\u01aa")
        buf.write("\u01ab\7*\2\2\u01abb\3\2\2\2\u01ac\u01ad\7+\2\2\u01ad")
        buf.write("d\3\2\2\2\u01ae\u01af\7}\2\2\u01aff\3\2\2\2\u01b0\u01b1")
        buf.write("\7\177\2\2\u01b1h\3\2\2\2\u01b2\u01b3\7]\2\2\u01b3j\3")
        buf.write("\2\2\2\u01b4\u01b5\7_\2\2\u01b5l\3\2\2\2\u01b6\u01b7\7")
        buf.write("<\2\2\u01b7n\3\2\2\2\u01b8\u01b9\7=\2\2\u01b9p\3\2\2\2")
        buf.write("\u01ba\u01bb\7.\2\2\u01bbr\3\2\2\2\u01bc\u01bd\7\60\2")
        buf.write("\2\u01bdt\3\2\2\2\u01be\u01c2\t\2\2\2\u01bf\u01c1\t\3")
        buf.write("\2\2\u01c0\u01bf\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3v\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c5\u01c6\5{>\2\u01c6\u01ca\7\60\2\2\u01c7")
        buf.write("\u01c9\t\4\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2")
        buf.write("\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01ce\3")
        buf.write("\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01cf\5y=\2\u01ce\u01cd")
        buf.write("\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01e1\3\2\2\2\u01d0")
        buf.write("\u01d2\7\60\2\2\u01d1\u01d3\t\4\2\2\u01d2\u01d1\3\2\2")
        buf.write("\2\u01d3\u01d4\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d8\5y=\2\u01d7\u01d6")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9")
        buf.write("\u01da\3\2\2\2\u01da\u01e1\3\2\2\2\u01db\u01dc\5{>\2\u01dc")
        buf.write("\u01dd\5y=\2\u01dd\u01e1\3\2\2\2\u01de\u01df\7\60\2\2")
        buf.write("\u01df\u01e1\5y=\2\u01e0\u01c5\3\2\2\2\u01e0\u01d0\3\2")
        buf.write("\2\2\u01e0\u01db\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e3\b<\2\2\u01e3x\3\2\2\2\u01e4\u01e6")
        buf.write("\t\5\2\2\u01e5\u01e7\t\6\2\2\u01e6\u01e5\3\2\2\2\u01e6")
        buf.write("\u01e7\3\2\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01ea\t\4\2\2")
        buf.write("\u01e9\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01e9\3")
        buf.write("\2\2\2\u01eb\u01ec\3\2\2\2\u01ecz\3\2\2\2\u01ed\u01f1")
        buf.write("\t\7\2\2\u01ee\u01f0\t\4\2\2\u01ef\u01ee\3\2\2\2\u01f0")
        buf.write("\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2")
        buf.write("\u01f2\u0201\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f6\7")
        buf.write("a\2\2\u01f5\u01f4\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5")
        buf.write("\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9")
        buf.write("\u01f7\3\2\2\2\u01fa\u01fc\t\4\2\2\u01fb\u01fa\3\2\2\2")
        buf.write("\u01fc\u01fd\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3")
        buf.write("\2\2\2\u01fe\u0200\3\2\2\2\u01ff\u01f7\3\2\2\2\u0200\u0203")
        buf.write("\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202")
        buf.write("\u0204\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0207\b>\3\2")
        buf.write("\u0205\u0207\7\62\2\2\u0206\u01ed\3\2\2\2\u0206\u0205")
        buf.write("\3\2\2\2\u0207|\3\2\2\2\u0208\u020c\7$\2\2\u0209\u020b")
        buf.write("\5\177@\2\u020a\u0209\3\2\2\2\u020b\u020e\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020f\3\2\2\2")
        buf.write("\u020e\u020c\3\2\2\2\u020f\u0210\7$\2\2\u0210\u0211\b")
        buf.write("?\4\2\u0211~\3\2\2\2\u0212\u0216\5\u0083B\2\u0213\u0216")
        buf.write("\n\b\2\2\u0214\u0216\5\u0081A\2\u0215\u0212\3\2\2\2\u0215")
        buf.write("\u0213\3\2\2\2\u0215\u0214\3\2\2\2\u0216\u0080\3\2\2\2")
        buf.write("\u0217\u0218\7^\2\2\u0218\u0219\t\t\2\2\u0219\u0082\3")
        buf.write("\2\2\2\u021a\u021b\7^\2\2\u021b\u021c\7$\2\2\u021c\u0084")
        buf.write("\3\2\2\2\u021d\u021f\t\n\2\2\u021e\u021d\3\2\2\2\u021f")
        buf.write("\u0220\3\2\2\2\u0220\u021e\3\2\2\2\u0220\u0221\3\2\2\2")
        buf.write("\u0221\u0222\3\2\2\2\u0222\u0223\bC\5\2\u0223\u0086\3")
        buf.write("\2\2\2\u0224\u0226\t\13\2\2\u0225\u0224\3\2\2\2\u0226")
        buf.write("\u0227\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3\2\2\2")
        buf.write("\u0228\u0229\3\2\2\2\u0229\u022a\bD\5\2\u022a\u022b\b")
        buf.write("D\6\2\u022b\u0088\3\2\2\2\u022c\u022d\7\61\2\2\u022d\u022e")
        buf.write("\7,\2\2\u022e\u0232\3\2\2\2\u022f\u0231\13\2\2\2\u0230")
        buf.write("\u022f\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0233\3\2\2\2")
        buf.write("\u0232\u0230\3\2\2\2\u0233\u0235\3\2\2\2\u0234\u0232\3")
        buf.write("\2\2\2\u0235\u0236\7,\2\2\u0236\u0237\7\61\2\2\u0237\u0238")
        buf.write("\3\2\2\2\u0238\u0239\bE\5\2\u0239\u008a\3\2\2\2\u023a")
        buf.write("\u023b\7\61\2\2\u023b\u023c\7\61\2\2\u023c\u0240\3\2\2")
        buf.write("\2\u023d\u023f\n\f\2\2\u023e\u023d\3\2\2\2\u023f\u0242")
        buf.write("\3\2\2\2\u0240\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241")
        buf.write("\u0243\3\2\2\2\u0242\u0240\3\2\2\2\u0243\u0244\bF\5\2")
        buf.write("\u0244\u008c\3\2\2\2\u0245\u0249\7$\2\2\u0246\u0248\5")
        buf.write("\177@\2\u0247\u0246\3\2\2\2\u0248\u024b\3\2\2\2\u0249")
        buf.write("\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024d\3\2\2\2")
        buf.write("\u024b\u0249\3\2\2\2\u024c\u024e\t\r\2\2\u024d\u024c\3")
        buf.write("\2\2\2\u024e\u024f\3\2\2\2\u024f\u0250\bG\7\2\u0250\u008e")
        buf.write("\3\2\2\2\u0251\u0252\7^\2\2\u0252\u0255\n\16\2\2\u0253")
        buf.write("\u0255\n\17\2\2\u0254\u0251\3\2\2\2\u0254\u0253\3\2\2")
        buf.write("\2\u0255\u0090\3\2\2\2\u0256\u025a\7$\2\2\u0257\u0259")
        buf.write("\5\177@\2\u0258\u0257\3\2\2\2\u0259\u025c\3\2\2\2\u025a")
        buf.write("\u0258\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u025d\3\2\2\2")
        buf.write("\u025c\u025a\3\2\2\2\u025d\u025e\5\u008fH\2\u025e\u025f")
        buf.write("\bI\b\2\u025f\u0092\3\2\2\2\u0260\u0261\13\2\2\2\u0261")
        buf.write("\u0262\bJ\t\2\u0262\u0094\3\2\2\2\32\2\u01c2\u01ca\u01ce")
        buf.write("\u01d4\u01d9\u01e0\u01e6\u01eb\u01f1\u01f7\u01fd\u0201")
        buf.write("\u0206\u020c\u0215\u0220\u0227\u0232\u0240\u0249\u024d")
        buf.write("\u0254\u025a\n\3<\2\3>\3\3?\4\b\2\2\4\2\2\3G\5\3I\6\3")
        buf.write("J\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FALSE = 6
    FLOAT = 7
    FOR = 8
    IF = 9
    INTEGER = 10
    RETURN = 11
    STRING = 12
    TRUE = 13
    WHILE = 14
    VOID = 15
    OUT = 16
    CONTINUE = 17
    OF = 18
    INHERIT = 19
    ARRAY = 20
    FUNC = 21
    READINT = 22
    PRINTINT = 23
    READF = 24
    WRITEF = 25
    READBOOL = 26
    PRINTBOOL = 27
    READSTRING = 28
    PRINTSTRING = 29
    SUPER = 30
    PREDE = 31
    ADD = 32
    SUB = 33
    MUL = 34
    DIV = 35
    MOD = 36
    NOT = 37
    AND = 38
    OR = 39
    EQUAL = 40
    NEQUAL = 41
    LT = 42
    LTE = 43
    GT = 44
    GTE = 45
    CONCAT = 46
    ASG = 47
    LB = 48
    RB = 49
    LP = 50
    RP = 51
    LS = 52
    RS = 53
    COLO = 54
    SEMI = 55
    COMMA = 56
    DOT = 57
    ID = 58
    FLOATLIT = 59
    INT = 60
    STRLIT = 61
    WS = 62
    WS1 = 63
    BLOCK_COMMENT = 64
    LINE_COMMENT = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67
    ERROR_CHAR = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'if'", "'integer'", "'return'", "'string'", 
            "'true'", "'while'", "'void'", "'out'", "'continue'", "'of'", 
            "'inherit'", "'array'", "'function'", "'readInteger'", "'printInteger'", 
            "'readFloat'", "'writeFloat'", "'readBoolean'", "'printBoolean'", 
            "'readString'", "'printString'", "'super'", "'preventDefault'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'='", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "':'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", 
            "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "FUNC", 
            "READINT", "PRINTINT", "READF", "WRITEF", "READBOOL", "PRINTBOOL", 
            "READSTRING", "PRINTSTRING", "SUPER", "PREDE", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NEQUAL", 
            "LT", "LTE", "GT", "GTE", "CONCAT", "ASG", "LB", "RB", "LP", 
            "RP", "LS", "RS", "COLO", "SEMI", "COMMA", "DOT", "ID", "FLOATLIT", 
            "INT", "STRLIT", "WS", "WS1", "BLOCK_COMMENT", "LINE_COMMENT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "FUNC", 
                  "READINT", "PRINTINT", "READF", "WRITEF", "READBOOL", 
                  "PRINTBOOL", "READSTRING", "PRINTSTRING", "SUPER", "PREDE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "NEQUAL", "LT", "LTE", "GT", "GTE", "CONCAT", 
                  "ASG", "LB", "RB", "LP", "RP", "LS", "RS", "COLO", "SEMI", 
                  "COMMA", "DOT", "ID", "FLOATLIT", "EXPONENT", "INT", "STRLIT", 
                  "STR_CHAR", "ESC_SEQ", "DOUQ", "WS", "WS1", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "UNCLOSE_STRING", "ESC_ILLEGAL", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.FLOATLIT_action 
            actions[60] = self.INT_action 
            actions[61] = self.STRLIT_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


