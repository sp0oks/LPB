from antlr4 import *
from LPBVisitor import LPBVisitor
from LPBParser import LPBParser
from LPBUtils import OutputParser, SymbolTable, Comodo

class SemanticAnalyzer(LPBVisitor):
    def __init__(self, out:OutputParser):
        self.out = out
        self.scopes = {}
        self.valido = True
        self.andar_atual = 0


    def visitPrograma(self, ctx:LPBParser.ProgramaContext):
    #   programa: 'imovel' decl_imovel ':' corpo 'fim_imovel'
        self.scopes['imovel'] = SymbolTable('imovel')
        self.scopes['imovel'].symbols['n_blocos'] = 0
        self.scopes['imovel'].symbols['n_andares'] = 0
        self.visitDecl_imovel(ctx.decl_imovel())
        if self.valido:
            self.visitCorpo(ctx.corpo())
            return self.scopes
        return None

    def visitDecl_casa(self, ctx:LPBParser.Decl_casaContext):
    #   decl_casa: 'Casa' '(' 'Tam' num_blocos=dimensao ',' 'Andares' num_andares=dimensao ')'
        blocos = self.visitDimensao(ctx.num_blocos)
        if blocos <= 0:
            self.out.write("Linha %d: número de blocos deve ser positivo." % ctx.start.line)
            self.valido = False
        else:
            self.scopes['imovel'].symbols['n_blocos'] = blocos
            l_blocos = {n_bloco:None for n_bloco in range(1, blocos+1)}
        andares = self.visitDimensao(ctx.num_andares)
        if andares not in [1,2]:
            self.out.write("Linha %d: número de andares do tipo Casa deve ser 1 ou 2." % ctx.start.line)
            self.valido = False
        if self.valido:
            self.scopes['imovel'].symbols['n_andares'] = andares
            self.scopes['andares'] = {n_andar:l_blocos.copy() for n_andar in range(1, andares+1)}
    

    def visitDecl_apartamento(self, ctx:LPBParser.Decl_apartamentoContext):
    #   decl_apartamento: 'Apartamento' '(' 'Tam' dimensao ')';
        blocos = self.visitDimensao(ctx.dimensao())
        if blocos <= 0:
            self.out.write("Linha %d: número de blocos deve ser positivo." % ctx.start.line)
            self.valido = False
        else:
            self.scopes['imovel'].symbols['n_blocos'] = blocos
            l_blocos = {n_bloco:None for n_bloco in range(1, blocos+1)}
        self.scopes['imovel'].symbols['n_andares'] = 1
        self.scopes['andares'] = {1:l_blocos}


    def visitDecl_andar(self, ctx:LPBParser.Decl_andarContext):
    #   decl_andar: 'andar' NUM_INT ':' decl_planta? 'fim_andar';
        num_andar = int(str(ctx.NUM_INT()))
        if num_andar not in range(1, self.scopes['imovel'].symbols['n_andares'] + 1):
            self.out.write("Linha %d: identificador de andar fora dos limites declarados." % ctx.start.line)
        else:
            self.andar_atual = num_andar
            if ctx.decl_planta() is None:
                self.out.write("Aviso: nenhum cômodo declarado no %dº andar." % num_andar)
            self.visitChildren(ctx)


    def visitDecl_planta(self, ctx:LPBParser.Decl_plantaContext):
    #   decl_planta: 'planta' ':' decl_comodos+ decl_moveis* 'fim_planta';
        for i in range(1, self.scopes['imovel'].symbols['n_blocos'] + 1):
            self.scopes['andares'][self.andar_atual][i] = SymbolTable("bloco[%d]" % i)
        self.visitChildren(ctx)
        if ctx.decl_moveis() is None:
            self.out.write("Aviso: nenhum móvel declarado no %dº andar." % self.andar_atual)
                
    
    def visitDecl_comodos(self, ctx:LPBParser.Decl_comodosContext):
    #   decl_comodos: id_bloco 'tem comodo' var_comodo (',' var_comodo)*;
        bloco = self.visitId_bloco(ctx.id_bloco())
        if bloco not in self.scopes['andares'][self.andar_atual]:
            self.out.write("Linha %d: identificador de bloco fora dos limites declarados." % ctx.start.line)
        else:
            for comodo in ctx.var_comodo():
                var = self.visitVar_comodo(comodo)
                if var.nome not in self.scopes['andares'][self.andar_atual][bloco].symbols:
                    self.scopes['andares'][self.andar_atual][bloco].symbols[var.nome] = var
                else:
                    self.out.write("Linha %d: variável %s já declarada anteriormente." % (ctx.start.line, var.nome))
  
    
    def visitVar_comodo(self, ctx:LPBParser.Var_comodoContext):
    #   var_comodo: IDENT tipo_comodo dimensao?;
        dim = 1
        if ctx.dimensao() is not None:
            dim = self.visitDimensao(ctx.dimensao())
        var_info = Comodo(ident=str(ctx.IDENT()), tipo=str(ctx.tipo_comodo().start.text), dimensao=dim)
        return var_info


    def visitDecl_moveis(self, ctx:LPBParser.Decl_moveisContext):
    #   decl_moveis: id_bloco '->' IDENT 'tem movel' tipo_movel (',' tipo_movel)*;
        bloco = self.visitId_bloco(ctx.id_bloco())
        if bloco not in self.scopes['andares'][self.andar_atual]:
            self.out.write("Linha %d: identificador de bloco fora dos limites declarados." % ctx.start.line)
        else:
            comodo = str(ctx.IDENT())
            if comodo not in self.scopes['andares'][self.andar_atual][bloco].symbols:
                self.out.write("Linha %d: variável %s não declarada." % (ctx.start.line, comodo))
            else:
                for tp_movel in ctx.tipo_movel():
                    movel = str(tp_movel.start.text)
                    self.scopes['andares'][self.andar_atual][bloco].symbols[comodo].moveis.append(movel)
        

    def visitId_bloco(self, ctx:LPBParser.Id_blocoContext):
    #   id_bloco: '{' NUM_INT '}';
        return int(str(ctx.NUM_INT()))


    def visitDimensao(self, ctx:LPBParser.DimensaoContext):
    #   dimensao: '[' NUM_INT ']';
        return int(str(ctx.NUM_INT()))
