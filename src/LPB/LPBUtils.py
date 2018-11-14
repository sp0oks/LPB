class OutputParser:
    def __init__(self):
        self.conteudo = ""
        self.modificado = False

    def isModificado(self):
        return self.modificado

    def write(self, texto):
        if not self.isModificado():
            self.modificado = True
        self.conteudo = "{}{}\n".format(self.conteudo,texto)

class SymbolTable:
    def __init__(self, scope):
        self.scope = scope
        self.symbols = {}

class Comodo:
    def __init__(self, ident, tipo, dimensao=1, moveis=None):
        self.nome = ident
        self.tipo = tipo
        self.dimensao = dimensao
        self.moveis = [] if moveis is None else moveis

