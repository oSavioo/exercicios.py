#Esse progrmaa faz com que você calcule seu imc e posteriormente saiba em qual categoria está
#Lembrando que foi pegado como fonte o "calculadora de IMC online"

while True:
    peso = int(input("Digite o seu peso(em kg): "))
    if peso > 0:
            break
    print("Valor inválido, digite um valor maior que zero!")

while True:
    altura = float(input("Digite o seu altura(em metros): "))
    if altura > 0:
            break
    print("Valor inválido, digite um valor maior que zero!")

imc = peso / altura **2

print("\n")

if imc<19.1:
    print("Está abaixo do peso")
elif imc >= 19.1 and imc <=25.8:
    print("Peso normal")
elif imc >= 25.8 and imc <= 27.3:
    print("Está um pouco acima do peso")
elif imc >= 27.4 and imc <= 32.3:
    print("Está acima do peso") 
elif imc >= 32.4:
    print ("Obesidade")

print("O valor do seu imc eh: ",round(imc,2))