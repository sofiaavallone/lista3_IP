nome_projeto = input()
componentes = [[]]

entrada = input()
while entrada != "Construir!":
    elemento = ""
    entrada_split = entrada.split(" ")
    for i in range(len(entrada_split)-1):
        elemento += (entrada_split[i] + " ")
    elemento2 = elemento.rstrip()
    if len(componentes) > 0:
        componentes[-1].append(elemento2)
        componentes[-1].append(entrada_split[-1])
    else:
        componentes[0].append(elemento2)
        componentes[0].append(entrada_split[-1])

    entrada = input()