# Generated from Python/src/stella/stellaLexer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2X")
        buf.write("\u027d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2")
        buf.write("\5\2\u00bc\n\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)")
        buf.write("\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\38\3")
        buf.write("8\38\38\38\38\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3")
        buf.write(";\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3")
        buf.write("?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3B\3")
        buf.write("B\3B\3B\3B\3C\3C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3D\3E\3E\3")
        buf.write("E\3E\3E\3F\3F\3F\3F\3F\3G\3G\3H\3H\3H\3H\3H\3H\3H\3H\3")
        buf.write("H\3H\3I\3I\3I\3I\3I\3I\3I\3I\3J\3J\3J\3J\3J\3K\3K\3K\3")
        buf.write("L\3L\3M\3M\3M\3M\3N\3N\3N\3N\3N\3N\3N\3O\3O\3O\3O\3O\3")
        buf.write("O\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3S\3S\3S\3")
        buf.write("S\3T\3T\3T\3T\7T\u022e\nT\fT\16T\u0231\13T\3T\5T\u0234")
        buf.write("\nT\3T\3T\5T\u0238\nT\3T\3T\3U\3U\3U\3U\7U\u0240\nU\f")
        buf.write("U\16U\u0243\13U\3U\3U\3U\3U\3U\3V\3V\5V\u024c\nV\3V\3")
        buf.write("V\3V\5V\u0251\nV\7V\u0253\nV\fV\16V\u0256\13V\3W\3W\3")
        buf.write("W\3W\5W\u025c\nW\6W\u025e\nW\rW\16W\u025f\3X\3X\3X\3X")
        buf.write("\3X\3X\6X\u0268\nX\rX\16X\u0269\3X\3X\3Y\6Y\u026f\nY\r")
        buf.write("Y\16Y\u0270\3Z\6Z\u0274\nZ\rZ\16Z\u0275\3Z\3Z\3[\3[\3")
        buf.write("\\\3\\\3\u0241\2]\3\2\5\2\7\2\t\2\13\3\r\4\17\5\21\6\23")
        buf.write("\7\25\b\27\t\31\n\33\13\35\f\37\r!\16#\17%\20\'\21)\22")
        buf.write("+\23-\24/\25\61\26\63\27\65\30\67\319\32;\33=\34?\35A")
        buf.write("\36C\37E G!I\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60g\61i\62")
        buf.write("k\63m\64o\65q\66s\67u8w9y:{;}<\177=\u0081>\u0083?\u0085")
        buf.write("@\u0087A\u0089B\u008bC\u008dD\u008fE\u0091F\u0093G\u0095")
        buf.write("H\u0097I\u0099J\u009bK\u009dL\u009fM\u00a1N\u00a3O\u00a5")
        buf.write("P\u00a7Q\u00a9R\u00abS\u00adT\u00afU\u00b1V\u00b3W\u00b5")
        buf.write("\2\u00b7X\3\2\13\5\2C\\\u00c2\u00d8\u00da\u00e0\5\2c|")
        buf.write("\u00e1\u00f8\u00fa\u0101\3\2\62;\4\2\f\f\17\17\7\2##/")
        buf.write("/<<AAaa\4\2//aa\3\2ch\5\2\13\f\16\17\"\"\b\2$$^^hhppt")
        buf.write("tvv\2\u0287\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2")
        buf.write("\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1")
        buf.write("\3\2\2\2\2\u00b3\3\2\2\2\2\u00b7\3\2\2\2\3\u00bb\3\2\2")
        buf.write("\2\5\u00bd\3\2\2\2\7\u00bf\3\2\2\2\t\u00c1\3\2\2\2\13")
        buf.write("\u00c3\3\2\2\2\r\u00c5\3\2\2\2\17\u00c7\3\2\2\2\21\u00c9")
        buf.write("\3\2\2\2\23\u00cb\3\2\2\2\25\u00cd\3\2\2\2\27\u00cf\3")
        buf.write("\2\2\2\31\u00d1\3\2\2\2\33\u00d3\3\2\2\2\35\u00d6\3\2")
        buf.write("\2\2\37\u00d9\3\2\2\2!\u00db\3\2\2\2#\u00de\3\2\2\2%\u00e1")
        buf.write("\3\2\2\2\'\u00e3\3\2\2\2)\u00e5\3\2\2\2+\u00e7\3\2\2\2")
        buf.write("-\u00ea\3\2\2\2/\u00ec\3\2\2\2\61\u00ef\3\2\2\2\63\u00f2")
        buf.write("\3\2\2\2\65\u00f5\3\2\2\2\67\u00f7\3\2\2\29\u00f9\3\2")
        buf.write("\2\2;\u00fb\3\2\2\2=\u00fd\3\2\2\2?\u00ff\3\2\2\2A\u010a")
        buf.write("\3\2\2\2C\u0118\3\2\2\2E\u0123\3\2\2\2G\u012d\3\2\2\2")
        buf.write("I\u0139\3\2\2\2K\u0142\3\2\2\2M\u0147\3\2\2\2O\u014b\3")
        buf.write("\2\2\2Q\u0150\3\2\2\2S\u0154\3\2\2\2U\u0157\3\2\2\2W\u015c")
        buf.write("\3\2\2\2Y\u0161\3\2\2\2[\u0166\3\2\2\2]\u016d\3\2\2\2")
        buf.write("_\u0173\3\2\2\2a\u0177\3\2\2\2c\u017a\3\2\2\2e\u017f\3")
        buf.write("\2\2\2g\u0182\3\2\2\2i\u0185\3\2\2\2k\u0189\3\2\2\2m\u0190")
        buf.write("\3\2\2\2o\u0194\3\2\2\2q\u019d\3\2\2\2s\u01a1\3\2\2\2")
        buf.write("u\u01a8\3\2\2\2w\u01ae\3\2\2\2y\u01b2\3\2\2\2{\u01b5\3")
        buf.write("\2\2\2}\u01bc\3\2\2\2\177\u01c1\3\2\2\2\u0081\u01c6\3")
        buf.write("\2\2\2\u0083\u01cd\3\2\2\2\u0085\u01d2\3\2\2\2\u0087\u01d7")
        buf.write("\3\2\2\2\u0089\u01de\3\2\2\2\u008b\u01e3\3\2\2\2\u008d")
        buf.write("\u01e8\3\2\2\2\u008f\u01ea\3\2\2\2\u0091\u01f4\3\2\2\2")
        buf.write("\u0093\u01fc\3\2\2\2\u0095\u0201\3\2\2\2\u0097\u0204\3")
        buf.write("\2\2\2\u0099\u0206\3\2\2\2\u009b\u020a\3\2\2\2\u009d\u0211")
        buf.write("\3\2\2\2\u009f\u0217\3\2\2\2\u00a1\u021b\3\2\2\2\u00a3")
        buf.write("\u0221\3\2\2\2\u00a5\u0225\3\2\2\2\u00a7\u0229\3\2\2\2")
        buf.write("\u00a9\u023b\3\2\2\2\u00ab\u024b\3\2\2\2\u00ad\u0257\3")
        buf.write("\2\2\2\u00af\u0261\3\2\2\2\u00b1\u026e\3\2\2\2\u00b3\u0273")
        buf.write("\3\2\2\2\u00b5\u0279\3\2\2\2\u00b7\u027b\3\2\2\2\u00b9")
        buf.write("\u00bc\5\5\3\2\u00ba\u00bc\5\7\4\2\u00bb\u00b9\3\2\2\2")
        buf.write("\u00bb\u00ba\3\2\2\2\u00bc\4\3\2\2\2\u00bd\u00be\t\2\2")
        buf.write("\2\u00be\6\3\2\2\2\u00bf\u00c0\t\3\2\2\u00c0\b\3\2\2\2")
        buf.write("\u00c1\u00c2\t\4\2\2\u00c2\n\3\2\2\2\u00c3\u00c4\7.\2")
        buf.write("\2\u00c4\f\3\2\2\2\u00c5\u00c6\7=\2\2\u00c6\16\3\2\2\2")
        buf.write("\u00c7\u00c8\7*\2\2\u00c8\20\3\2\2\2\u00c9\u00ca\7+\2")
        buf.write("\2\u00ca\22\3\2\2\2\u00cb\u00cc\7}\2\2\u00cc\24\3\2\2")
        buf.write("\2\u00cd\u00ce\7\177\2\2\u00ce\26\3\2\2\2\u00cf\u00d0")
        buf.write("\7?\2\2\u00d0\30\3\2\2\2\u00d1\u00d2\7<\2\2\u00d2\32\3")
        buf.write("\2\2\2\u00d3\u00d4\7/\2\2\u00d4\u00d5\7@\2\2\u00d5\34")
        buf.write("\3\2\2\2\u00d6\u00d7\7?\2\2\u00d7\u00d8\7@\2\2\u00d8\36")
        buf.write("\3\2\2\2\u00d9\u00da\7~\2\2\u00da \3\2\2\2\u00db\u00dc")
        buf.write("\7>\2\2\u00dc\u00dd\7~\2\2\u00dd\"\3\2\2\2\u00de\u00df")
        buf.write("\7~\2\2\u00df\u00e0\7@\2\2\u00e0$\3\2\2\2\u00e1\u00e2")
        buf.write("\7]\2\2\u00e2&\3\2\2\2\u00e3\u00e4\7_\2\2\u00e4(\3\2\2")
        buf.write("\2\u00e5\u00e6\7>\2\2\u00e6*\3\2\2\2\u00e7\u00e8\7>\2")
        buf.write("\2\u00e8\u00e9\7?\2\2\u00e9,\3\2\2\2\u00ea\u00eb\7@\2")
        buf.write("\2\u00eb.\3\2\2\2\u00ec\u00ed\7@\2\2\u00ed\u00ee\7?\2")
        buf.write("\2\u00ee\60\3\2\2\2\u00ef\u00f0\7?\2\2\u00f0\u00f1\7?")
        buf.write("\2\2\u00f1\62\3\2\2\2\u00f2\u00f3\7#\2\2\u00f3\u00f4\7")
        buf.write("?\2\2\u00f4\64\3\2\2\2\u00f5\u00f6\7-\2\2\u00f6\66\3\2")
        buf.write("\2\2\u00f7\u00f8\7/\2\2\u00f88\3\2\2\2\u00f9\u00fa\7,")
        buf.write("\2\2\u00fa:\3\2\2\2\u00fb\u00fc\7\61\2\2\u00fc<\3\2\2")
        buf.write("\2\u00fd\u00fe\7\60\2\2\u00fe>\3\2\2\2\u00ff\u0100\7N")
        buf.write("\2\2\u0100\u0101\7k\2\2\u0101\u0102\7u\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103\u0104\7<\2\2\u0104\u0105\7<\2\2\u0105\u0106")
        buf.write("\7j\2\2\u0106\u0107\7g\2\2\u0107\u0108\7c\2\2\u0108\u0109")
        buf.write("\7f\2\2\u0109@\3\2\2\2\u010a\u010b\7N\2\2\u010b\u010c")
        buf.write("\7k\2\2\u010c\u010d\7u\2\2\u010d\u010e\7v\2\2\u010e\u010f")
        buf.write("\7<\2\2\u010f\u0110\7<\2\2\u0110\u0111\7k\2\2\u0111\u0112")
        buf.write("\7u\2\2\u0112\u0113\7g\2\2\u0113\u0114\7o\2\2\u0114\u0115")
        buf.write("\7r\2\2\u0115\u0116\7v\2\2\u0116\u0117\7{\2\2\u0117B\3")
        buf.write("\2\2\2\u0118\u0119\7N\2\2\u0119\u011a\7k\2\2\u011a\u011b")
        buf.write("\7u\2\2\u011b\u011c\7v\2\2\u011c\u011d\7<\2\2\u011d\u011e")
        buf.write("\7<\2\2\u011e\u011f\7v\2\2\u011f\u0120\7c\2\2\u0120\u0121")
        buf.write("\7k\2\2\u0121\u0122\7n\2\2\u0122D\3\2\2\2\u0123\u0124")
        buf.write("\7P\2\2\u0124\u0125\7c\2\2\u0125\u0126\7v\2\2\u0126\u0127")
        buf.write("\7<\2\2\u0127\u0128\7<\2\2\u0128\u0129\7r\2\2\u0129\u012a")
        buf.write("\7t\2\2\u012a\u012b\7g\2\2\u012b\u012c\7f\2\2\u012cF\3")
        buf.write("\2\2\2\u012d\u012e\7P\2\2\u012e\u012f\7c\2\2\u012f\u0130")
        buf.write("\7v\2\2\u0130\u0131\7<\2\2\u0131\u0132\7<\2\2\u0132\u0133")
        buf.write("\7k\2\2\u0133\u0134\7u\2\2\u0134\u0135\7|\2\2\u0135\u0136")
        buf.write("\7g\2\2\u0136\u0137\7t\2\2\u0137\u0138\7q\2\2\u0138H\3")
        buf.write("\2\2\2\u0139\u013a\7P\2\2\u013a\u013b\7c\2\2\u013b\u013c")
        buf.write("\7v\2\2\u013c\u013d\7<\2\2\u013d\u013e\7<\2\2\u013e\u013f")
        buf.write("\7t\2\2\u013f\u0140\7g\2\2\u0140\u0141\7e\2\2\u0141J\3")
        buf.write("\2\2\2\u0142\u0143\7D\2\2\u0143\u0144\7q\2\2\u0144\u0145")
        buf.write("\7q\2\2\u0145\u0146\7n\2\2\u0146L\3\2\2\2\u0147\u0148")
        buf.write("\7P\2\2\u0148\u0149\7c\2\2\u0149\u014a\7v\2\2\u014aN\3")
        buf.write("\2\2\2\u014b\u014c\7W\2\2\u014c\u014d\7p\2\2\u014d\u014e")
        buf.write("\7k\2\2\u014e\u014f\7v\2\2\u014fP\3\2\2\2\u0150\u0151")
        buf.write("\7c\2\2\u0151\u0152\7p\2\2\u0152\u0153\7f\2\2\u0153R\3")
        buf.write("\2\2\2\u0154\u0155\7c\2\2\u0155\u0156\7u\2\2\u0156T\3")
        buf.write("\2\2\2\u0157\u0158\7e\2\2\u0158\u0159\7q\2\2\u0159\u015a")
        buf.write("\7p\2\2\u015a\u015b\7u\2\2\u015bV\3\2\2\2\u015c\u015d")
        buf.write("\7e\2\2\u015d\u015e\7q\2\2\u015e\u015f\7t\2\2\u015f\u0160")
        buf.write("\7g\2\2\u0160X\3\2\2\2\u0161\u0162\7g\2\2\u0162\u0163")
        buf.write("\7n\2\2\u0163\u0164\7u\2\2\u0164\u0165\7g\2\2\u0165Z\3")
        buf.write("\2\2\2\u0166\u0167\7g\2\2\u0167\u0168\7z\2\2\u0168\u0169")
        buf.write("\7v\2\2\u0169\u016a\7g\2\2\u016a\u016b\7p\2\2\u016b\u016c")
        buf.write("\7f\2\2\u016c\\\3\2\2\2\u016d\u016e\7h\2\2\u016e\u016f")
        buf.write("\7c\2\2\u016f\u0170\7n\2\2\u0170\u0171\7u\2\2\u0171\u0172")
        buf.write("\7g\2\2\u0172^\3\2\2\2\u0173\u0174\7h\2\2\u0174\u0175")
        buf.write("\7k\2\2\u0175\u0176\7z\2\2\u0176`\3\2\2\2\u0177\u0178")
        buf.write("\7h\2\2\u0178\u0179\7p\2\2\u0179b\3\2\2\2\u017a\u017b")
        buf.write("\7h\2\2\u017b\u017c\7q\2\2\u017c\u017d\7n\2\2\u017d\u017e")
        buf.write("\7f\2\2\u017ed\3\2\2\2\u017f\u0180\7k\2\2\u0180\u0181")
        buf.write("\7h\2\2\u0181f\3\2\2\2\u0182\u0183\7k\2\2\u0183\u0184")
        buf.write("\7p\2\2\u0184h\3\2\2\2\u0185\u0186\7k\2\2\u0186\u0187")
        buf.write("\7p\2\2\u0187\u0188\7n\2\2\u0188j\3\2\2\2\u0189\u018a")
        buf.write("\7k\2\2\u018a\u018b\7p\2\2\u018b\u018c\7n\2\2\u018c\u018d")
        buf.write("\7k\2\2\u018d\u018e\7p\2\2\u018e\u018f\7g\2\2\u018fl\3")
        buf.write("\2\2\2\u0190\u0191\7k\2\2\u0191\u0192\7p\2\2\u0192\u0193")
        buf.write("\7t\2\2\u0193n\3\2\2\2\u0194\u0195\7n\2\2\u0195\u0196")
        buf.write("\7c\2\2\u0196\u0197\7p\2\2\u0197\u0198\7i\2\2\u0198\u0199")
        buf.write("\7w\2\2\u0199\u019a\7c\2\2\u019a\u019b\7i\2\2\u019b\u019c")
        buf.write("\7g\2\2\u019cp\3\2\2\2\u019d\u019e\7n\2\2\u019e\u019f")
        buf.write("\7g\2\2\u019f\u01a0\7v\2\2\u01a0r\3\2\2\2\u01a1\u01a2")
        buf.write("\7n\2\2\u01a2\u01a3\7g\2\2\u01a3\u01a4\7v\2\2\u01a4\u01a5")
        buf.write("\7t\2\2\u01a5\u01a6\7g\2\2\u01a6\u01a7\7e\2\2\u01a7t\3")
        buf.write("\2\2\2\u01a8\u01a9\7o\2\2\u01a9\u01aa\7c\2\2\u01aa\u01ab")
        buf.write("\7v\2\2\u01ab\u01ac\7e\2\2\u01ac\u01ad\7j\2\2\u01adv\3")
        buf.write("\2\2\2\u01ae\u01af\7p\2\2\u01af\u01b0\7q\2\2\u01b0\u01b1")
        buf.write("\7v\2\2\u01b1x\3\2\2\2\u01b2\u01b3\7q\2\2\u01b3\u01b4")
        buf.write("\7t\2\2\u01b4z\3\2\2\2\u01b5\u01b6\7t\2\2\u01b6\u01b7")
        buf.write("\7g\2\2\u01b7\u01b8\7v\2\2\u01b8\u01b9\7w\2\2\u01b9\u01ba")
        buf.write("\7t\2\2\u01ba\u01bb\7p\2\2\u01bb|\3\2\2\2\u01bc\u01bd")
        buf.write("\7u\2\2\u01bd\u01be\7w\2\2\u01be\u01bf\7e\2\2\u01bf\u01c0")
        buf.write("\7e\2\2\u01c0~\3\2\2\2\u01c1\u01c2\7v\2\2\u01c2\u01c3")
        buf.write("\7j\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5\7p\2\2\u01c5\u0080")
        buf.write("\3\2\2\2\u01c6\u01c7\7v\2\2\u01c7\u01c8\7j\2\2\u01c8\u01c9")
        buf.write("\7t\2\2\u01c9\u01ca\7q\2\2\u01ca\u01cb\7y\2\2\u01cb\u01cc")
        buf.write("\7u\2\2\u01cc\u0082\3\2\2\2\u01cd\u01ce\7v\2\2\u01ce\u01cf")
        buf.write("\7t\2\2\u01cf\u01d0\7w\2\2\u01d0\u01d1\7g\2\2\u01d1\u0084")
        buf.write("\3\2\2\2\u01d2\u01d3\7v\2\2\u01d3\u01d4\7{\2\2\u01d4\u01d5")
        buf.write("\7r\2\2\u01d5\u01d6\7g\2\2\u01d6\u0086\3\2\2\2\u01d7\u01d8")
        buf.write("\7w\2\2\u01d8\u01d9\7p\2\2\u01d9\u01da\7h\2\2\u01da\u01db")
        buf.write("\7q\2\2\u01db\u01dc\7n\2\2\u01dc\u01dd\7f\2\2\u01dd\u0088")
        buf.write("\3\2\2\2\u01de\u01df\7w\2\2\u01df\u01e0\7p\2\2\u01e0\u01e1")
        buf.write("\7k\2\2\u01e1\u01e2\7v\2\2\u01e2\u008a\3\2\2\2\u01e3\u01e4")
        buf.write("\7y\2\2\u01e4\u01e5\7k\2\2\u01e5\u01e6\7v\2\2\u01e6\u01e7")
        buf.write("\7j\2\2\u01e7\u008c\3\2\2\2\u01e8\u01e9\7\u00b7\2\2\u01e9")
        buf.write("\u008e\3\2\2\2\u01ea\u01eb\7g\2\2\u01eb\u01ec\7z\2\2\u01ec")
        buf.write("\u01ed\7e\2\2\u01ed\u01ee\7g\2\2\u01ee\u01ef\7r\2\2\u01ef")
        buf.write("\u01f0\7v\2\2\u01f0\u01f1\7k\2\2\u01f1\u01f2\7q\2\2\u01f2")
        buf.write("\u01f3\7p\2\2\u01f3\u0090\3\2\2\2\u01f4\u01f5\7x\2\2\u01f5")
        buf.write("\u01f6\7c\2\2\u01f6\u01f7\7t\2\2\u01f7\u01f8\7k\2\2\u01f8")
        buf.write("\u01f9\7c\2\2\u01f9\u01fa\7p\2\2\u01fa\u01fb\7v\2\2\u01fb")
        buf.write("\u0092\3\2\2\2\u01fc\u01fd\7e\2\2\u01fd\u01fe\7c\2\2\u01fe")
        buf.write("\u01ff\7u\2\2\u01ff\u0200\7v\2\2\u0200\u0094\3\2\2\2\u0201")
        buf.write("\u0202\7<\2\2\u0202\u0203\7?\2\2\u0203\u0096\3\2\2\2\u0204")
        buf.write("\u0205\7(\2\2\u0205\u0098\3\2\2\2\u0206\u0207\7p\2\2\u0207")
        buf.write("\u0208\7g\2\2\u0208\u0209\7y\2\2\u0209\u009a\3\2\2\2\u020a")
        buf.write("\u020b\7r\2\2\u020b\u020c\7c\2\2\u020c\u020d\7p\2\2\u020d")
        buf.write("\u020e\7k\2\2\u020e\u020f\7e\2\2\u020f\u0210\7#\2\2\u0210")
        buf.write("\u009c\3\2\2\2\u0211\u0212\7v\2\2\u0212\u0213\7j\2\2\u0213")
        buf.write("\u0214\7t\2\2\u0214\u0215\7q\2\2\u0215\u0216\7y\2\2\u0216")
        buf.write("\u009e\3\2\2\2\u0217\u0218\7v\2\2\u0218\u0219\7t\2\2\u0219")
        buf.write("\u021a\7{\2\2\u021a\u00a0\3\2\2\2\u021b\u021c\7e\2\2\u021c")
        buf.write("\u021d\7c\2\2\u021d\u021e\7v\2\2\u021e\u021f\7e\2\2\u021f")
        buf.write("\u0220\7j\2\2\u0220\u00a2\3\2\2\2\u0221\u0222\7V\2\2\u0222")
        buf.write("\u0223\7q\2\2\u0223\u0224\7r\2\2\u0224\u00a4\3\2\2\2\u0225")
        buf.write("\u0226\7D\2\2\u0226\u0227\7q\2\2\u0227\u0228\7v\2\2\u0228")
        buf.write("\u00a6\3\2\2\2\u0229\u022a\7\61\2\2\u022a\u022b\7\61\2")
        buf.write("\2\u022b\u022f\3\2\2\2\u022c\u022e\n\5\2\2\u022d\u022c")
        buf.write("\3\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2\u022f")
        buf.write("\u0230\3\2\2\2\u0230\u0237\3\2\2\2\u0231\u022f\3\2\2\2")
        buf.write("\u0232\u0234\7\17\2\2\u0233\u0232\3\2\2\2\u0233\u0234")
        buf.write("\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0238\7\f\2\2\u0236")
        buf.write("\u0238\7\2\2\3\u0237\u0233\3\2\2\2\u0237\u0236\3\2\2\2")
        buf.write("\u0238\u0239\3\2\2\2\u0239\u023a\bT\2\2\u023a\u00a8\3")
        buf.write("\2\2\2\u023b\u023c\7\61\2\2\u023c\u023d\7,\2\2\u023d\u0241")
        buf.write("\3\2\2\2\u023e\u0240\13\2\2\2\u023f\u023e\3\2\2\2\u0240")
        buf.write("\u0243\3\2\2\2\u0241\u0242\3\2\2\2\u0241\u023f\3\2\2\2")
        buf.write("\u0242\u0244\3\2\2\2\u0243\u0241\3\2\2\2\u0244\u0245\7")
        buf.write(",\2\2\u0245\u0246\7\61\2\2\u0246\u0247\3\2\2\2\u0247\u0248")
        buf.write("\bU\2\2\u0248\u00aa\3\2\2\2\u0249\u024c\7a\2\2\u024a\u024c")
        buf.write("\5\3\2\2\u024b\u0249\3\2\2\2\u024b\u024a\3\2\2\2\u024c")
        buf.write("\u0254\3\2\2\2\u024d\u0253\t\6\2\2\u024e\u0251\5\t\5\2")
        buf.write("\u024f\u0251\5\3\2\2\u0250\u024e\3\2\2\2\u0250\u024f\3")
        buf.write("\2\2\2\u0251\u0253\3\2\2\2\u0252\u024d\3\2\2\2\u0252\u0250")
        buf.write("\3\2\2\2\u0253\u0256\3\2\2\2\u0254\u0252\3\2\2\2\u0254")
        buf.write("\u0255\3\2\2\2\u0255\u00ac\3\2\2\2\u0256\u0254\3\2\2\2")
        buf.write("\u0257\u025d\7%\2\2\u0258\u025e\t\7\2\2\u0259\u025c\5")
        buf.write("\t\5\2\u025a\u025c\5\3\2\2\u025b\u0259\3\2\2\2\u025b\u025a")
        buf.write("\3\2\2\2\u025c\u025e\3\2\2\2\u025d\u0258\3\2\2\2\u025d")
        buf.write("\u025b\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u025d\3\2\2\2")
        buf.write("\u025f\u0260\3\2\2\2\u0260\u00ae\3\2\2\2\u0261\u0262\7")
        buf.write(">\2\2\u0262\u0263\7\62\2\2\u0263\u0264\7z\2\2\u0264\u0267")
        buf.write("\3\2\2\2\u0265\u0268\5\t\5\2\u0266\u0268\t\b\2\2\u0267")
        buf.write("\u0265\3\2\2\2\u0267\u0266\3\2\2\2\u0268\u0269\3\2\2\2")
        buf.write("\u0269\u0267\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u026b\3")
        buf.write("\2\2\2\u026b\u026c\7@\2\2\u026c\u00b0\3\2\2\2\u026d\u026f")
        buf.write("\5\t\5\2\u026e\u026d\3\2\2\2\u026f\u0270\3\2\2\2\u0270")
        buf.write("\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u00b2\3\2\2\2")
        buf.write("\u0272\u0274\t\t\2\2\u0273\u0272\3\2\2\2\u0274\u0275\3")
        buf.write("\2\2\2\u0275\u0273\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0277")
        buf.write("\3\2\2\2\u0277\u0278\bZ\2\2\u0278\u00b4\3\2\2\2\u0279")
        buf.write("\u027a\t\n\2\2\u027a\u00b6\3\2\2\2\u027b\u027c\13\2\2")
        buf.write("\2\u027c\u00b8\3\2\2\2\23\2\u00bb\u022f\u0233\u0237\u0241")
        buf.write("\u024b\u0250\u0252\u0254\u025b\u025d\u025f\u0267\u0269")
        buf.write("\u0270\u0275\3\b\2\2")
        return buf.getvalue()


class stellaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Surrogate_id_SYMB_0 = 1
    Surrogate_id_SYMB_1 = 2
    Surrogate_id_SYMB_2 = 3
    Surrogate_id_SYMB_3 = 4
    Surrogate_id_SYMB_4 = 5
    Surrogate_id_SYMB_5 = 6
    Surrogate_id_SYMB_6 = 7
    Surrogate_id_SYMB_7 = 8
    Surrogate_id_SYMB_8 = 9
    Surrogate_id_SYMB_9 = 10
    Surrogate_id_SYMB_10 = 11
    Surrogate_id_SYMB_11 = 12
    Surrogate_id_SYMB_12 = 13
    Surrogate_id_SYMB_13 = 14
    Surrogate_id_SYMB_14 = 15
    Surrogate_id_SYMB_15 = 16
    Surrogate_id_SYMB_16 = 17
    Surrogate_id_SYMB_17 = 18
    Surrogate_id_SYMB_18 = 19
    Surrogate_id_SYMB_19 = 20
    Surrogate_id_SYMB_20 = 21
    Surrogate_id_SYMB_21 = 22
    Surrogate_id_SYMB_22 = 23
    Surrogate_id_SYMB_23 = 24
    Surrogate_id_SYMB_24 = 25
    Surrogate_id_SYMB_25 = 26
    Surrogate_id_SYMB_26 = 27
    Surrogate_id_SYMB_27 = 28
    Surrogate_id_SYMB_28 = 29
    Surrogate_id_SYMB_29 = 30
    Surrogate_id_SYMB_30 = 31
    Surrogate_id_SYMB_31 = 32
    Surrogate_id_SYMB_32 = 33
    Surrogate_id_SYMB_33 = 34
    Surrogate_id_SYMB_34 = 35
    Surrogate_id_SYMB_35 = 36
    Surrogate_id_SYMB_36 = 37
    Surrogate_id_SYMB_37 = 38
    Surrogate_id_SYMB_38 = 39
    Surrogate_id_SYMB_39 = 40
    Surrogate_id_SYMB_40 = 41
    Surrogate_id_SYMB_41 = 42
    Surrogate_id_SYMB_42 = 43
    Surrogate_id_SYMB_43 = 44
    Surrogate_id_SYMB_44 = 45
    Surrogate_id_SYMB_45 = 46
    Surrogate_id_SYMB_46 = 47
    Surrogate_id_SYMB_47 = 48
    Surrogate_id_SYMB_48 = 49
    Surrogate_id_SYMB_49 = 50
    Surrogate_id_SYMB_50 = 51
    Surrogate_id_SYMB_51 = 52
    Surrogate_id_SYMB_52 = 53
    Surrogate_id_SYMB_53 = 54
    Surrogate_id_SYMB_54 = 55
    Surrogate_id_SYMB_55 = 56
    Surrogate_id_SYMB_56 = 57
    Surrogate_id_SYMB_57 = 58
    Surrogate_id_SYMB_58 = 59
    Surrogate_id_SYMB_59 = 60
    Surrogate_id_SYMB_60 = 61
    Surrogate_id_SYMB_61 = 62
    Surrogate_id_SYMB_62 = 63
    Surrogate_id_SYMB_63 = 64
    Surrogate_id_SYMB_64 = 65
    Surrogate_id_SYMB_65 = 66
    EXCEPTION = 67
    VARIANT = 68
    CAST = 69
    ASSIGN = 70
    REF_TYPE = 71
    REFERENCE = 72
    PANIC = 73
    THROW = 74
    TRY = 75
    CATCH = 76
    TOP_TYPE = 77
    BOTTOM_TYPE = 78
    COMMENT_antlr_builtin = 79
    MULTICOMMENT_antlr_builtin = 80
    StellaIdent = 81
    ExtensionName = 82
    MemoryAddress = 83
    INTEGER = 84
    WS = 85
    ErrorToken = 86

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "'('", "')'", "'{'", "'}'", "'='", "':'", "'->'", 
            "'=>'", "'|'", "'<|'", "'|>'", "'['", "']'", "'<'", "'<='", 
            "'>'", "'>='", "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", "'.'", 
            "'List::head'", "'List::isempty'", "'List::tail'", "'Nat::pred'", 
            "'Nat::iszero'", "'Nat::rec'", "'Bool'", "'Nat'", "'Unit'", 
            "'and'", "'as'", "'cons'", "'core'", "'else'", "'extend'", "'false'", 
            "'fix'", "'fn'", "'fold'", "'if'", "'in'", "'inl'", "'inline'", 
            "'inr'", "'language'", "'let'", "'letrec'", "'match'", "'not'", 
            "'or'", "'return'", "'succ'", "'then'", "'throws'", "'true'", 
            "'type'", "'unfold'", "'unit'", "'with'", "'\u00B5'", "'exception'", 
            "'variant'", "'cast'", "':='", "'&'", "'new'", "'panic!'", "'throw'", 
            "'try'", "'catch'", "'Top'", "'Bot'" ]

    symbolicNames = [ "<INVALID>",
            "Surrogate_id_SYMB_0", "Surrogate_id_SYMB_1", "Surrogate_id_SYMB_2", 
            "Surrogate_id_SYMB_3", "Surrogate_id_SYMB_4", "Surrogate_id_SYMB_5", 
            "Surrogate_id_SYMB_6", "Surrogate_id_SYMB_7", "Surrogate_id_SYMB_8", 
            "Surrogate_id_SYMB_9", "Surrogate_id_SYMB_10", "Surrogate_id_SYMB_11", 
            "Surrogate_id_SYMB_12", "Surrogate_id_SYMB_13", "Surrogate_id_SYMB_14", 
            "Surrogate_id_SYMB_15", "Surrogate_id_SYMB_16", "Surrogate_id_SYMB_17", 
            "Surrogate_id_SYMB_18", "Surrogate_id_SYMB_19", "Surrogate_id_SYMB_20", 
            "Surrogate_id_SYMB_21", "Surrogate_id_SYMB_22", "Surrogate_id_SYMB_23", 
            "Surrogate_id_SYMB_24", "Surrogate_id_SYMB_25", "Surrogate_id_SYMB_26", 
            "Surrogate_id_SYMB_27", "Surrogate_id_SYMB_28", "Surrogate_id_SYMB_29", 
            "Surrogate_id_SYMB_30", "Surrogate_id_SYMB_31", "Surrogate_id_SYMB_32", 
            "Surrogate_id_SYMB_33", "Surrogate_id_SYMB_34", "Surrogate_id_SYMB_35", 
            "Surrogate_id_SYMB_36", "Surrogate_id_SYMB_37", "Surrogate_id_SYMB_38", 
            "Surrogate_id_SYMB_39", "Surrogate_id_SYMB_40", "Surrogate_id_SYMB_41", 
            "Surrogate_id_SYMB_42", "Surrogate_id_SYMB_43", "Surrogate_id_SYMB_44", 
            "Surrogate_id_SYMB_45", "Surrogate_id_SYMB_46", "Surrogate_id_SYMB_47", 
            "Surrogate_id_SYMB_48", "Surrogate_id_SYMB_49", "Surrogate_id_SYMB_50", 
            "Surrogate_id_SYMB_51", "Surrogate_id_SYMB_52", "Surrogate_id_SYMB_53", 
            "Surrogate_id_SYMB_54", "Surrogate_id_SYMB_55", "Surrogate_id_SYMB_56", 
            "Surrogate_id_SYMB_57", "Surrogate_id_SYMB_58", "Surrogate_id_SYMB_59", 
            "Surrogate_id_SYMB_60", "Surrogate_id_SYMB_61", "Surrogate_id_SYMB_62", 
            "Surrogate_id_SYMB_63", "Surrogate_id_SYMB_64", "Surrogate_id_SYMB_65", 
            "EXCEPTION", "VARIANT", "CAST", "ASSIGN", "REF_TYPE", "REFERENCE", 
            "PANIC", "THROW", "TRY", "CATCH", "TOP_TYPE", "BOTTOM_TYPE", 
            "COMMENT_antlr_builtin", "MULTICOMMENT_antlr_builtin", "StellaIdent", 
            "ExtensionName", "MemoryAddress", "INTEGER", "WS", "ErrorToken" ]

    ruleNames = [ "LETTER", "CAPITAL", "SMALL", "DIGIT", "Surrogate_id_SYMB_0", 
                  "Surrogate_id_SYMB_1", "Surrogate_id_SYMB_2", "Surrogate_id_SYMB_3", 
                  "Surrogate_id_SYMB_4", "Surrogate_id_SYMB_5", "Surrogate_id_SYMB_6", 
                  "Surrogate_id_SYMB_7", "Surrogate_id_SYMB_8", "Surrogate_id_SYMB_9", 
                  "Surrogate_id_SYMB_10", "Surrogate_id_SYMB_11", "Surrogate_id_SYMB_12", 
                  "Surrogate_id_SYMB_13", "Surrogate_id_SYMB_14", "Surrogate_id_SYMB_15", 
                  "Surrogate_id_SYMB_16", "Surrogate_id_SYMB_17", "Surrogate_id_SYMB_18", 
                  "Surrogate_id_SYMB_19", "Surrogate_id_SYMB_20", "Surrogate_id_SYMB_21", 
                  "Surrogate_id_SYMB_22", "Surrogate_id_SYMB_23", "Surrogate_id_SYMB_24", 
                  "Surrogate_id_SYMB_25", "Surrogate_id_SYMB_26", "Surrogate_id_SYMB_27", 
                  "Surrogate_id_SYMB_28", "Surrogate_id_SYMB_29", "Surrogate_id_SYMB_30", 
                  "Surrogate_id_SYMB_31", "Surrogate_id_SYMB_32", "Surrogate_id_SYMB_33", 
                  "Surrogate_id_SYMB_34", "Surrogate_id_SYMB_35", "Surrogate_id_SYMB_36", 
                  "Surrogate_id_SYMB_37", "Surrogate_id_SYMB_38", "Surrogate_id_SYMB_39", 
                  "Surrogate_id_SYMB_40", "Surrogate_id_SYMB_41", "Surrogate_id_SYMB_42", 
                  "Surrogate_id_SYMB_43", "Surrogate_id_SYMB_44", "Surrogate_id_SYMB_45", 
                  "Surrogate_id_SYMB_46", "Surrogate_id_SYMB_47", "Surrogate_id_SYMB_48", 
                  "Surrogate_id_SYMB_49", "Surrogate_id_SYMB_50", "Surrogate_id_SYMB_51", 
                  "Surrogate_id_SYMB_52", "Surrogate_id_SYMB_53", "Surrogate_id_SYMB_54", 
                  "Surrogate_id_SYMB_55", "Surrogate_id_SYMB_56", "Surrogate_id_SYMB_57", 
                  "Surrogate_id_SYMB_58", "Surrogate_id_SYMB_59", "Surrogate_id_SYMB_60", 
                  "Surrogate_id_SYMB_61", "Surrogate_id_SYMB_62", "Surrogate_id_SYMB_63", 
                  "Surrogate_id_SYMB_64", "Surrogate_id_SYMB_65", "EXCEPTION", 
                  "VARIANT", "CAST", "ASSIGN", "REF_TYPE", "REFERENCE", 
                  "PANIC", "THROW", "TRY", "CATCH", "TOP_TYPE", "BOTTOM_TYPE", 
                  "COMMENT_antlr_builtin", "MULTICOMMENT_antlr_builtin", 
                  "StellaIdent", "ExtensionName", "MemoryAddress", "INTEGER", 
                  "WS", "Escapable", "ErrorToken" ]

    grammarFileName = "stellaLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


