sentenca = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"

PALAVRA_PROCURADA = "little"

def contador_de_palavras(sentenca):
    # separar string em lista de palavras
    palavras = []
    sentenca_split = sentenca.lower().split()
    for palavra in sentenca_split:
        palavras.append(palavra)
    
    # conta quantos littles
    contagem_palavras = 0
    for palavra in palavras:
        if palavra == PALAVRA_PROCURADA:
            contagem_palavras += 1
    
    print(f'''
          A palavra procurada *{PALAVRA_PROCURADA}* aparece {contagem_palavras} vezes na sentença\n''')

contador_de_palavras(sentenca)