sentenca = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"

def contador_de_littles(sentenca):
    # separar string em lista de palavras
    palavras = []
    sentenca_split = sentenca.lower().split()
    for palavra in sentenca_strip:
        palavras.append(palavra)
    print(palavras)
    
    # conta quantos littles
    contagem_littles = 0
    for palavra in palavras:
        if palavra == "little":
            contagem_littles += 1
    
    print(f"A palavra little aparece {contagem_littles} vezes na sentença")


contador_de_littles(sentenca)