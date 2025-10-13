lista_convidados = []
lista_comidas =[]
valor_comida = []

num_convidados = int(input())
passou = 0
for i in range(num_convidados):
    nome = input()
    if nome == "Maicon Kuster":
        print("você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
    else:
        lista_convidados.append(nome)

        comida = input()
        if len(lista_comidas) >= 1:
            chave = True
            for repetida in lista_comidas and chave == True:
                if repetida == comida:
                    print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {lista_convidados.index(i)}")
                    lista_convidados.pop()
                else:
                    lista_comidas.append(comida)
                    valor_comida.append(input())
                    passou+=1
                    chave = False
        else:
            lista_comidas.append(comida)
            valor_comida.append(input())
            passou+=1

if passou == 0 or len(lista_convidados) == 0:
    print("Nenhum convidado marcou presença na festa do calabreso!")
else:
    # Informações correspondentes a comida mais cara
    valor_comida_cara = max(valor_comida)
    i_comida_cara = valor_comida.index(valor_comida_cara)
    pessoa_comida_cara = lista_convidados[i_comida_cara]
    comida_cara = lista_comidas[i_comida_cara]
    print(f"Obrigado para o(a) {pessoa_comida_cara} pelo(a) excelente {comida_cara}")

    if len(lista_convidados) > 1:
        # Informações correspondentes a comida mais barata
        valor_comida_barata = min(valor_comida)
        i_comida_barata = valor_comida.index(valor_comida_barata)
        pessoa_comida_barata = lista_convidados[i_comida_barata]
        comida_barata = lista_comidas[i_comida_barata]
        print(f"Rapaz, {pessoa_comida_barata} trouxe o(a) {comida_barata} que estava altamente mais ou menos!!!")

print("Lista de convidados do Calabreso")

valor_comida_ordenada = valor_comida.copy()
valor_ordenada = valor_comida_ordenada.sort()
for valor in valor_comida_ordenada:
    i_antigo = valor_comida.index(valor)
    i_novo = valor_comida_ordenada.index(valor)
    
    for nome in lista_convidados:
        lista_convidados[i_novo] = lista_convidados[i_antigo]

print("Lista de convidados do Calabreso")
for nome in lista_convidados:
    j = 0
    print(f"{j+1}- {nome}")