# Generated from LPB.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LPBParser import LPBParser
else:
    from LPBParser import LPBParser
from antlr4.error.Errors import ParseCancellationException

# This class defines a complete generic visitor for a parse tree produced by LPBParser.

class LPBVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LPBParser#programa.
    def visitPrograma(self, ctx:LPBParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#decl_imovel.
    def visitDecl_imovel(self, ctx:LPBParser.Decl_imovelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#decl_casa.
    def visitDecl_casa(self, ctx:LPBParser.Decl_casaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#decl_apartamento.
    def visitDecl_apartamento(self, ctx:LPBParser.Decl_apartamentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#corpo.
    def visitCorpo(self, ctx:LPBParser.CorpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#decl_andar.
    def visitDecl_andar(self, ctx:LPBParser.Decl_andarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#decl_planta.
    def visitDecl_planta(self, ctx:LPBParser.Decl_plantaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#decl_comodos.
    def visitDecl_comodos(self, ctx:LPBParser.Decl_comodosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#decl_moveis.
    def visitDecl_moveis(self, ctx:LPBParser.Decl_moveisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#id_bloco.
    def visitId_bloco(self, ctx:LPBParser.Id_blocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#var_comodo.
    def visitVar_comodo(self, ctx:LPBParser.Var_comodoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#tipo_comodo.
    def visitTipo_comodo(self, ctx:LPBParser.Tipo_comodoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#tipo_movel.
    def visitTipo_movel(self, ctx:LPBParser.Tipo_movelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#dimensao.
    def visitDimensao(self, ctx:LPBParser.DimensaoContext):
        return self.visitChildren(ctx)



del LPBParser