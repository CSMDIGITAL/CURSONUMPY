class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"Produto: {self.nome} | Preço: R$ {self.preco:.2f}")


nome_informado = input("Nome do produto: ")
preco_informado = float(input("Preço do produto: "))

p = Produto(nome_informado, preco_informado)

p.exibir()