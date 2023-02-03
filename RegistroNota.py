from Nota import Nota

class RegistroNota:
    def __init__(self):
        self.nota = Nota

    def cadastro_nota(self, valor:int):
        self.valor_nota = self.nota(valor,1)
        return self.valor_nota

    def quantidade_nota(self, valor:int):
        quantidade = self.nota.quantidade
        return quantidade
    
    def adicionar_nota(self, valor:int, quantidade:int):
        self.valor_nota = valor
        self.quantidade_nota += quantidade
        self.nota(self.valor_nota, self.quantidade_nota)

    def retirar_nota(self, valor: int, qnt_origem: int, quantidade:int):
        valor_nota = valor
        quantidade_nota = qnt_origem
        quantidade_nota -= quantidade
        self.nota(valor_nota, quantidade_nota)
