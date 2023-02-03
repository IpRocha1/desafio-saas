from RegistroNota import RegistroNota

class ValidaSaque:
    def __init__(self):
        self.registro = RegistroNota()
        self.notas = [
            self.registro.cadastro_nota(100),
            self.registro.cadastro_nota(50),
            self.registro.cadastro_nota(20),
            self.registro.cadastro_nota(10)
        ]
    
    def verifica_notas(self, valor_saque:int):
        saque_quantidade = []
        saque_notas = []
        valor_sacado = valor_saque
        if valor_saque <= 0:
            print("Valor de saque errado. Tente novamente.")
        elif valor_saque <= self.soma_total_caixa():
            for self.nota in self.notas:
                if self.nota.quantidade_nota > 0 and valor_saque >= self.nota.valor_nota:
                    quantidade = valor_saque // self.nota.valor_nota
                    if quantidade <= self.nota.quantidade_nota:
                        valor_saque -= quantidade*self.nota.valor_nota
                        self.registro.retirar_nota(self.nota.valor_nota, self.nota.quantidade_nota, quantidade)
                        saque_quantidade.append(quantidade)
                        saque_notas.append(self.nota.valor_nota)
                        if valor_saque == 0:
                            break
            print("Para o saque de R$",valor_sacado,",00 - Notas liberadas para saque:")
            cont = 0
            for self.saques in saque_quantidade:
                print(self.saques,"nota de R$",saque_notas[cont],",00")
                cont +=1
        
        else:
            print("Quantidade de notas insuficientes no caixa")
        if valor_saque > 0:
            print("Quantidade de notas insuficientes para saque")
        


    def soma_total_caixa(self):
        soma = 0
        for self.nota in self.notas:
            soma += self.nota.quantidade_nota*self.nota.valor_nota
        return soma


valida = ValidaSaque()
valida.verifica_notas(0)
valida.verifica_notas(10)
valida.verifica_notas(120)
valida.verifica_notas(120)
