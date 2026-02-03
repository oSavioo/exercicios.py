# Exercicio 1015 do beecrowd, nele calculamos a seguinte expressão sqrt((x2-x1)^2) + ((y2-y1)^2)


x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
resultado = ((x2 - x1) **2) + ((y2 - y1)**2)
resultado = resultado **0.5
print(round(resultado,4))
