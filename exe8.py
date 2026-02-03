"""#  Crie uma lista de 5 frutas e verifique se a fruta faz parte da lista"""

frutas = ['pera', 'abacaxi', 'uva', 'morango', 'melao']

fruta = input("Digite o nome da fruta para verificarmos se está na lista: ") .strip() .lower()

if fruta in frutas:
    print ("A fruta está na lista")
else:
    print("A fruta não está na lista")