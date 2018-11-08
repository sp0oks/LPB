from antlr4 import *
from LPBVisitor import LPBVisitor
from LPBParser import LPBParser
from LPBUtils import OutputParser, SymbolTable

class SemanticAnalyzer(LPBVisitor):
    def __init__(self, out:OutputParser):
        self.out = out
        self.scopes = {}

    def visitPrograma(self, ctx:LPBParser.ProgramaContext):
    #   programa: 'imovel' decl_imovel ':' corpo 'fim_imovel'
        self.scopes['imovel'] = SymbolTable('imovel')
        self.scopes['imovel'].symbols['n_blocos'] = 0
        self.scopes['imovel'].symbols['n_andares'] = 0
        self.visitChildren(ctx)

    def visitDecl_casa(self, ctx:LPBParser.Decl_casaContext):
    #   decl_casa: 'Casa' '(' 'Tam' num_blocos=dimensao ',' 'Andares' num_andares=dimensao ')'
        blocos = self.visitDimensao(ctx.num_blocos)
        self.scopes['imovel'].symbols['n_blocos'] = blocos
        if blocos <= 0:
            #[print(x, " => ", y, end=", ") for x, y in vars(ctx).items()]
            self.out.write("Linha %d: número de blocos deve ser positivo." % ctx.start.line)
        
        andares = self.visitDimensao(ctx.num_andares)
        self.scopes['imovel'].symbols['n_andares'] = andares
        if andares not in [1,2]:
            #[print(x, " => ", y) for x, y in vars(ctx).items()]
            self.out.write("Linha %d: número de andares do tipo Casa deve ser 1 ou 2." % ctx.start.line)

    
    def visitDecl_apartamento(self, ctx:LPBParser.Decl_apartamentoContext):
    #   decl_apartamento: 'Apartamento' '(' 'Tam' dimensao ')';
        blocos = self.visitDimensao(ctx.dimensao)
        self.scopes['imovel'].symbols['n_blocos'] = blocos
        if blocos <= 0:
            #[print(x, " => ", y, end=", ") for x, y in vars(ctx).items()]
            self.out.write("Linha %d: número de blocos deve ser positivo." % ctx.start.line)
        self.scopes['imovel'].symbols['n_andares'] = 1


    def visitDecl_andar(self, ctx:LPBParser.Decl_andarContext):
    #   decl_andar: 'andar' NUM_INT ':' decl_planta? 'fim_andar';
        num_andar = int(str(ctx.NUM_INT()))
        if num_andar not in range(1, self.scopes['imovel'].symbols['n_andares'] + 1):
            self.out.write("Linha %d: identificador de andar fora dos limites declarados." % ctx.start.line)
        self.visitChildren(ctx)


    def visitDecl_planta(self, ctx:LPBParser.Decl_plantaContext):
    #   decl_planta: 'planta' ':' decl_comodos+ decl_moveis* 'fim_planta';
        self.scopes['blocos'] = {}
        for i in range(1, self.scopes['imovel'].symbols['n_blocos'] + 1):
            self.scopes['blocos'][i] = SymbolTable("bloco[%d]" % i)
        self.visitChildren(ctx)
        
    
    def visitDecl_comodos(self, ctx:LPBParser.Decl_comodosContext):
    #   decl_comodos: id_bloco 'tem comodo' var_comodo (',' var_comodo)*;
        id_bloco = self.visitId_bloco(ctx.id_bloco())
        if id_bloco not in range(1, self.scopes['imovel'].symbols['n_blocos'] + 1):
            self.out.write("Linha %d: identificador de bloco fora dos limites declarados." % ctx.start.line)
        else:
            for comodo in ctx.var_comodo():
                id_comodo = comodo.start.text
                if id_comodo not in self.scopes['blocos'][id_bloco].symbols:
                    self.scopes['blocos'][id_bloco].symbols[id_comodo] = 'comodo'
                else:
                    self.out.write("Linha %d: variável %s já declarada anteriormente." % (ctx.start.line, id_comodo))
  

    def visitId_bloco(self, ctx:LPBParser.Id_blocoContext):
    #   id_bloco: '{' NUM_INT '}';
        return int(str(ctx.NUM_INT()))


    def visitDimensao(self, ctx:LPBParser.DimensaoContext):
    #   dimensao: '[' NUM_INT ']';
        return int(str(ctx.NUM_INT()))
