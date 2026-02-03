"""Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"""

dias_semana = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']

while True:
    dia = input("Digite um dia da semana: ").strip().lower()

    if dia in dias_semana:
        break
    else:
        print("Dia inválido! Digite: segunda, terca, quarta, quinta, sexta, sabado ou domingo.")

if dia == 'sabado' or dia == 'domingo':
    print ("Hoje é dia de descanso")
else:
    print("Hoje é dia de trabalhar")