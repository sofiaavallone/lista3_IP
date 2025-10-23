eventos = [] # Personagem, tipo de evento, hora início e hora fim
nivel_suspeita = 0

numero_eventos = int(input())
# Recebendo as informações e adicionando na matriz
for i in range(numero_eventos):
    entrada = input()
    linha_matriz = entrada.split(" - ")
    eventos.append(linha_matriz)

# Bubble sort para ordenar os eventos cronologicamente (Regra 0)
for i in range(len(eventos)-1):
    for j in range(len(eventos)-i-1):
        hora_inicio = int(eventos[j][-2].replace(":", ""))
        hora_inicio2 = int(eventos[j+1][-2].replace(":", ""))
        if hora_inicio < hora_inicio2:
            eventos[j], eventos[j+1] = eventos[j+1], eventos[j]

chave = False
i = 0
while i < len(eventos) and chave == False:
    personagem = eventos[i][0]
    evento = eventos[i][1]
    inicio = eventos[i][2]
    fim = eventos[i][3]

    v = False
    jm = False
    zf = False


    # Regra 1
    if personagem == "VJM":
        chave = True
        nivel_suspeita = 100
    i += 1