preco = float(input("Digite o preço do produto: "))
desconto_percentual = float(input("Digite o percentual de desconto: "))


valor_desconto = preco * (desconto_percentual / 100)
preco_final = preco - valor_desconto

print(f"O valor final com desconto é: R$ {preco_final:.2f}")