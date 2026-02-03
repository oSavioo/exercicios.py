#Exercicio para a verificação da classificação dos lados dos triângulos


num1= int(input())
num2= int(input())
num3= int(input())

if num1 == num2 == num3:
    print("Triângulo Equilátero")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Triângulo Isóceles")
else:
    print("Triângulo Escaleno")