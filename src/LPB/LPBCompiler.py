#! /usr/bin/python3
import sys
import json
from antlr4.error.Errors import ParseCancellationException
from antlr4 import *
from LPBUtils import OutputParser
from LPBLexer import LPBLexer
from LPBParser import LPBParser
from LPBSemantics import SemanticAnalyzer
from LPBGenerator import ImageGenerator

def main(argv):
    out = OutputParser()
    try:
        in_file = FileStream(argv[1])
        lexer = LPBLexer(in_file)
        stream = CommonTokenStream(lexer)
        parser = LPBParser(stream)
        tree = parser.programa()
    #    out.write(tree.toStringTree(recog=parser))
    except ParseCancellationException as pce:
        out.write("Erro: " + str(pce))
    except IndexError:
        print("Erro: não foram encontrados arquivos de entrada para o compilador.")
    except FileNotFoundError:
        print("Erro: arquivo de entrada inexistente.")

    if not out.isModificado():
        sem = SemanticAnalyzer(out)
        simbolos = sem.visitPrograma(tree)
        if not out.isModificado():
            if simbolos is not None:
                if len(argv) >= 3:
                    imgen = ImageGenerator(simbolos, sys.argv[2])
                else:
                    imgen = ImageGenerator(simbolos, "result")
                imgen.generate()
        else:
            out.write("Fim da compilação.")
    else:
        out.write("Fim da compilação.")
    print(out.conteudo)


if __name__ == '__main__':
    main(sys.argv)
