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
            j = 0
            repetida = False
            for palavra in lista_comidas:
                if chave == True:
                    if palavra == comida:
                        repetida = True
                j+=1
                if j == len(lista_comidas):
                    chave = False
            
            if repetida == True:
                print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {lista_convidados[-1]}")
                lista_convidados.pop()
            else:
                lista_comidas.append(comida)
                valor_comida.append(int(input()))
                passou+=1
        else:
            lista_comidas.append(comida)
            valor_comida.append(int(input()))
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

n = len(valor_comida)
for i in range(n-1):
    for j in range(n-i-1):
        if valor_comida[j] > valor_comida[j+1]:
            valor_comida[j], valor_comida[j+1] = valor_comida[j+1], valor_comida[j]
            lista_convidados[j], lista_convidados[j+1] = lista_convidados[j+1], lista_convidados[j]
        elif valor_comida[j] == valor_comida[j+1]:
            nomes_iguais = lista_convidados[j:j+1]
            nomes_ordenados = nomes_iguais.sort()
            for k in range(len(nomes_iguais)):
                lista_convidados[j], lista_convidados[j+1] = nomes_iguais[k], nomes_iguais[k+1]

print("Lista de convidados do Calabreso")
for z in range(len(lista_convidados)):
    for nome in lista_convidados:
        print(f"{z+1}- {nome}")