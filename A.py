frases = ['Que tiro foi esse?', 'Segura a marimba', 'Tá com raiva? Morde as costas', 'Bateu de frente é só rajadão']
quant_novas_frases = int(input())

for i in range(quant_novas_frases):
    frases.append(input())

for frase in frases:
    print(f'{frase}')