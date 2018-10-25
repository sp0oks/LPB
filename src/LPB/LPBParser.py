# Generated from LPB.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\5\3#\n\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\6")
        buf.write("\6\67\n\6\r\6\16\68\3\6\7\6<\n\6\f\6\16\6?\13\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\7\7H\n\7\f\7\16\7K\13\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\nZ\n\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\2\2\16\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\2\4\3\2\24\30\3\2\31 \2\\\2\32")
        buf.write("\3\2\2\2\4\"\3\2\2\2\6$\3\2\2\2\b-\3\2\2\2\n\63\3\2\2")
        buf.write("\2\fB\3\2\2\2\16L\3\2\2\2\20R\3\2\2\2\22V\3\2\2\2\24[")
        buf.write("\3\2\2\2\26]\3\2\2\2\30_\3\2\2\2\32\33\7\3\2\2\33\34\5")
        buf.write("\4\3\2\34\35\7\4\2\2\35\36\5\n\6\2\36\37\7\5\2\2\37\3")
        buf.write("\3\2\2\2 #\5\6\4\2!#\5\b\5\2\" \3\2\2\2\"!\3\2\2\2#\5")
        buf.write("\3\2\2\2$%\7\6\2\2%&\7\7\2\2&\'\7\b\2\2\'(\5\30\r\2()")
        buf.write("\7\t\2\2)*\7\n\2\2*+\5\30\r\2+,\7\13\2\2,\7\3\2\2\2-.")
        buf.write("\7\f\2\2./\7\7\2\2/\60\7\b\2\2\60\61\5\30\r\2\61\62\7")
        buf.write("\13\2\2\62\t\3\2\2\2\63\64\7\r\2\2\64\66\7\4\2\2\65\67")
        buf.write("\5\f\7\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2")
        buf.write("\29=\3\2\2\2:<\5\16\b\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2\2")
        buf.write("=>\3\2\2\2>@\3\2\2\2?=\3\2\2\2@A\7\16\2\2A\13\3\2\2\2")
        buf.write("BC\5\20\t\2CD\7\17\2\2DI\5\22\n\2EF\7\t\2\2FH\5\22\n\2")
        buf.write("GE\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J\r\3\2\2\2KI")
        buf.write("\3\2\2\2LM\5\20\t\2MN\7\20\2\2NO\7$\2\2OP\7\21\2\2PQ\5")
        buf.write("\26\f\2Q\17\3\2\2\2RS\7\22\2\2ST\7#\2\2TU\7\23\2\2U\21")
        buf.write("\3\2\2\2VW\7$\2\2WY\5\24\13\2XZ\5\30\r\2YX\3\2\2\2YZ\3")
        buf.write("\2\2\2Z\23\3\2\2\2[\\\t\2\2\2\\\25\3\2\2\2]^\t\3\2\2^")
        buf.write("\27\3\2\2\2_`\7!\2\2`a\7#\2\2ab\7\"\2\2b\31\3\2\2\2\7")
        buf.write("\"8=IY")
        return buf.getvalue()


class LPBParser ( Parser ):

    grammarFileName = "LPB.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'imovel'", "':'", "'fim_imovel'", "'Casa'", 
                     "'('", "'Tam'", "','", "'Andares'", "')'", "'Apartamento'", 
                     "'planta'", "'fim_planta'", "'tem comodo'", "'->'", 
                     "'tem movel'", "'{'", "'}'", "'cozinha'", "'quarto'", 
                     "'banheiro'", "'quintal'", "'escritorio'", "'sofa'", 
                     "'cama'", "'armario'", "'pia'", "'chuveiro'", "'televisao'", 
                     "'geladeira'", "'piscina'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM_INT", "IDENT", "ESPACO", "COMENT", 
                      "COMENT_N_FECHADO", "SIMB_DESCONHECIDO" ]

    RULE_programa = 0
    RULE_decl_imovel = 1
    RULE_decl_casa = 2
    RULE_decl_apartamento = 3
    RULE_decl_planta = 4
    RULE_decl_comodos = 5
    RULE_decl_moveis = 6
    RULE_id_quadrante = 7
    RULE_var_comodo = 8
    RULE_tipo_comodo = 9
    RULE_tipo_movel = 10
    RULE_dimensao = 11

    ruleNames =  [ "programa", "decl_imovel", "decl_casa", "decl_apartamento", 
                   "decl_planta", "decl_comodos", "decl_moveis", "id_quadrante", 
                   "var_comodo", "tipo_comodo", "tipo_movel", "dimensao" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    NUM_INT=33
    IDENT=34
    ESPACO=35
    COMENT=36
    COMENT_N_FECHADO=37
    SIMB_DESCONHECIDO=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_imovel(self):
            return self.getTypedRuleContext(LPBParser.Decl_imovelContext,0)


        def decl_planta(self):
            return self.getTypedRuleContext(LPBParser.Decl_plantaContext,0)


        def getRuleIndex(self):
            return LPBParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = LPBParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(LPBParser.T__0)
            self.state = 25
            self.decl_imovel()
            self.state = 26
            self.match(LPBParser.T__1)
            self.state = 27
            self.decl_planta()
            self.state = 28
            self.match(LPBParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Decl_imovelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_casa(self):
            return self.getTypedRuleContext(LPBParser.Decl_casaContext,0)


        def decl_apartamento(self):
            return self.getTypedRuleContext(LPBParser.Decl_apartamentoContext,0)


        def getRuleIndex(self):
            return LPBParser.RULE_decl_imovel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_imovel" ):
                listener.enterDecl_imovel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_imovel" ):
                listener.exitDecl_imovel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_imovel" ):
                return visitor.visitDecl_imovel(self)
            else:
                return visitor.visitChildren(self)




    def decl_imovel(self):

        localctx = LPBParser.Decl_imovelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_imovel)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LPBParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.decl_casa()
                pass
            elif token in [LPBParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.decl_apartamento()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Decl_casaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.num_andares = None # DimensaoContext

        def dimensao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPBParser.DimensaoContext)
            else:
                return self.getTypedRuleContext(LPBParser.DimensaoContext,i)


        def getRuleIndex(self):
            return LPBParser.RULE_decl_casa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_casa" ):
                listener.enterDecl_casa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_casa" ):
                listener.exitDecl_casa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_casa" ):
                return visitor.visitDecl_casa(self)
            else:
                return visitor.visitChildren(self)




    def decl_casa(self):

        localctx = LPBParser.Decl_casaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl_casa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(LPBParser.T__3)
            self.state = 35
            self.match(LPBParser.T__4)
            self.state = 36
            self.match(LPBParser.T__5)
            self.state = 37
            self.dimensao()
            self.state = 38
            self.match(LPBParser.T__6)
            self.state = 39
            self.match(LPBParser.T__7)
            self.state = 40
            localctx.num_andares = self.dimensao()
            self.state = 41
            self.match(LPBParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Decl_apartamentoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimensao(self):
            return self.getTypedRuleContext(LPBParser.DimensaoContext,0)


        def getRuleIndex(self):
            return LPBParser.RULE_decl_apartamento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_apartamento" ):
                listener.enterDecl_apartamento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_apartamento" ):
                listener.exitDecl_apartamento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_apartamento" ):
                return visitor.visitDecl_apartamento(self)
            else:
                return visitor.visitChildren(self)




    def decl_apartamento(self):

        localctx = LPBParser.Decl_apartamentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl_apartamento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(LPBParser.T__9)
            self.state = 44
            self.match(LPBParser.T__4)
            self.state = 45
            self.match(LPBParser.T__5)
            self.state = 46
            self.dimensao()
            self.state = 47
            self.match(LPBParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Decl_plantaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_comodos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPBParser.Decl_comodosContext)
            else:
                return self.getTypedRuleContext(LPBParser.Decl_comodosContext,i)


        def decl_moveis(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPBParser.Decl_moveisContext)
            else:
                return self.getTypedRuleContext(LPBParser.Decl_moveisContext,i)


        def getRuleIndex(self):
            return LPBParser.RULE_decl_planta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_planta" ):
                listener.enterDecl_planta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_planta" ):
                listener.exitDecl_planta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_planta" ):
                return visitor.visitDecl_planta(self)
            else:
                return visitor.visitChildren(self)




    def decl_planta(self):

        localctx = LPBParser.Decl_plantaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl_planta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(LPBParser.T__10)
            self.state = 50
            self.match(LPBParser.T__1)
            self.state = 52 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 51
                    self.decl_comodos()

                else:
                    raise NoViableAltException(self)
                self.state = 54 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LPBParser.T__15:
                self.state = 56
                self.decl_moveis()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(LPBParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Decl_comodosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_quadrante(self):
            return self.getTypedRuleContext(LPBParser.Id_quadranteContext,0)


        def var_comodo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LPBParser.Var_comodoContext)
            else:
                return self.getTypedRuleContext(LPBParser.Var_comodoContext,i)


        def getRuleIndex(self):
            return LPBParser.RULE_decl_comodos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_comodos" ):
                listener.enterDecl_comodos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_comodos" ):
                listener.exitDecl_comodos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_comodos" ):
                return visitor.visitDecl_comodos(self)
            else:
                return visitor.visitChildren(self)




    def decl_comodos(self):

        localctx = LPBParser.Decl_comodosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_decl_comodos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.id_quadrante()
            self.state = 65
            self.match(LPBParser.T__12)
            self.state = 66
            self.var_comodo()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LPBParser.T__6:
                self.state = 67
                self.match(LPBParser.T__6)
                self.state = 68
                self.var_comodo()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Decl_moveisContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_quadrante(self):
            return self.getTypedRuleContext(LPBParser.Id_quadranteContext,0)


        def IDENT(self):
            return self.getToken(LPBParser.IDENT, 0)

        def tipo_movel(self):
            return self.getTypedRuleContext(LPBParser.Tipo_movelContext,0)


        def getRuleIndex(self):
            return LPBParser.RULE_decl_moveis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_moveis" ):
                listener.enterDecl_moveis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_moveis" ):
                listener.exitDecl_moveis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_moveis" ):
                return visitor.visitDecl_moveis(self)
            else:
                return visitor.visitChildren(self)




    def decl_moveis(self):

        localctx = LPBParser.Decl_moveisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl_moveis)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.id_quadrante()
            self.state = 75
            self.match(LPBParser.T__13)
            self.state = 76
            self.match(LPBParser.IDENT)
            self.state = 77
            self.match(LPBParser.T__14)
            self.state = 78
            self.tipo_movel()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Id_quadranteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(LPBParser.NUM_INT, 0)

        def getRuleIndex(self):
            return LPBParser.RULE_id_quadrante

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_quadrante" ):
                listener.enterId_quadrante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_quadrante" ):
                listener.exitId_quadrante(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_quadrante" ):
                return visitor.visitId_quadrante(self)
            else:
                return visitor.visitChildren(self)




    def id_quadrante(self):

        localctx = LPBParser.Id_quadranteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_id_quadrante)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(LPBParser.T__15)
            self.state = 81
            self.match(LPBParser.NUM_INT)
            self.state = 82
            self.match(LPBParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_comodoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LPBParser.IDENT, 0)

        def tipo_comodo(self):
            return self.getTypedRuleContext(LPBParser.Tipo_comodoContext,0)


        def dimensao(self):
            return self.getTypedRuleContext(LPBParser.DimensaoContext,0)


        def getRuleIndex(self):
            return LPBParser.RULE_var_comodo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_comodo" ):
                listener.enterVar_comodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_comodo" ):
                listener.exitVar_comodo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_comodo" ):
                return visitor.visitVar_comodo(self)
            else:
                return visitor.visitChildren(self)




    def var_comodo(self):

        localctx = LPBParser.Var_comodoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_comodo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(LPBParser.IDENT)
            self.state = 85
            self.tipo_comodo()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LPBParser.T__30:
                self.state = 86
                self.dimensao()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tipo_comodoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LPBParser.RULE_tipo_comodo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo_comodo" ):
                listener.enterTipo_comodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo_comodo" ):
                listener.exitTipo_comodo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo_comodo" ):
                return visitor.visitTipo_comodo(self)
            else:
                return visitor.visitChildren(self)




    def tipo_comodo(self):

        localctx = LPBParser.Tipo_comodoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tipo_comodo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LPBParser.T__17) | (1 << LPBParser.T__18) | (1 << LPBParser.T__19) | (1 << LPBParser.T__20) | (1 << LPBParser.T__21))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tipo_movelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LPBParser.RULE_tipo_movel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo_movel" ):
                listener.enterTipo_movel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo_movel" ):
                listener.exitTipo_movel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo_movel" ):
                return visitor.visitTipo_movel(self)
            else:
                return visitor.visitChildren(self)




    def tipo_movel(self):

        localctx = LPBParser.Tipo_movelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_tipo_movel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LPBParser.T__22) | (1 << LPBParser.T__23) | (1 << LPBParser.T__24) | (1 << LPBParser.T__25) | (1 << LPBParser.T__26) | (1 << LPBParser.T__27) | (1 << LPBParser.T__28) | (1 << LPBParser.T__29))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DimensaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(LPBParser.NUM_INT, 0)

        def getRuleIndex(self):
            return LPBParser.RULE_dimensao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimensao" ):
                listener.enterDimensao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimensao" ):
                listener.exitDimensao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensao" ):
                return visitor.visitDimensao(self)
            else:
                return visitor.visitChildren(self)




    def dimensao(self):

        localctx = LPBParser.DimensaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dimensao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(LPBParser.T__30)
            self.state = 94
            self.match(LPBParser.NUM_INT)
            self.state = 95
            self.match(LPBParser.T__31)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





