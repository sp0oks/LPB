# Generated from LPB.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LPBParser import LPBParser
else:
    from LPBParser import LPBParser

# This class defines a complete generic visitor for a parse tree produced by LPBParser.

class LPBVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LPBParser#planta.
    def visitPlanta(self, ctx:LPBParser.PlantaContext):
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


    # Visit a parse tree produced by LPBParser#id_quadrante.
    def visitId_quadrante(self, ctx:LPBParser.Id_quadranteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#posicao.
    def visitPosicao(self, ctx:LPBParser.PosicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#expr_quadrante.
    def visitExpr_quadrante(self, ctx:LPBParser.Expr_quadranteContext):
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


    # Visit a parse tree produced by LPBParser#id_comodo.
    def visitId_comodo(self, ctx:LPBParser.Id_comodoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#id_movel.
    def visitId_movel(self, ctx:LPBParser.Id_movelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#expr_posicao.
    def visitExpr_posicao(self, ctx:LPBParser.Expr_posicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LPBParser#tipo_comodo.
    def visitTipo_comodo(self, ctx:LPBParser.Tipo_comodoContext):
        return self.visitChildren(ctx)



del LPBParser