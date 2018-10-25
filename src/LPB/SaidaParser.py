class SaidaParser:
    def __init__(self):
        self.conteudo = ""
        self.modificado = False

    def isModificado(self):
        return self.modificado

    def write(self, texto):
        if not self.isModificado():
            self.modificado = True
        self.conteudo+=texto

