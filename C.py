goleiros = []
hab_goleiros = []
treinos = []
goleiros_especiais = ["Rokenedy", "IShowSpeed", "Sérgio Soares", "Neymar Jr", "Gabriel Vasconcelos"]

n_treinos = int(input())
hab_inicial_luva = int(input())
sequencia_treinos = input()
treinos_split = sequencia_treinos.split("-")
for i in range(len(treinos_split)):
    if i%2 == 0:
        goleiros.append(treinos_split[i])
    else:
        treinos.append(treinos_split[i])

