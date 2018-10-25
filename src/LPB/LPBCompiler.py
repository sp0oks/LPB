import sys
from antlr4 import *
from LPBLexer import LPBLexer
from LPBParser import LPBParser


def main(argv):
    try:
        input = FileStream(argv[1])
        lexer = LPBLexer(input)
        stream = CommonTokenStream(lexer)
        parser = LPBParser(stream)
        tree = parser.programa()
        print(tree.toStringTree(recog=parser))

    except IndexError:
        print("Erro: não foram encontrados arquivos de entrada para o compilador.")

    except FileNotFoundError:
        print("Erro: arquivo de entrada inexistente.")


if __name__ == '__main__':
    main(sys.argv)