estoque = ["caneta", "caderno", "borracha", "lapis"]
print(estoque)

#adicionar novo item ao estoque
estoque.append("marcador")
print(estoque)

#remover item do estoque
estoque.remove("lapis")
print(estoque)

#verificar se um item esta em estoque
print("borracha" in estoque) #saída: true
print("apontador" in estoque) #saída: true