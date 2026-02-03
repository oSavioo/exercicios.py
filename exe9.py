# Faça um programa que conte quantas vezes a letra "a" aparece na música, também contando quantas palavras e quantas letras tem no total da letra
# A música é quero ver o oco de raimundos  

musica = """Fizera pouco em tê-lo deixado todo quebrado
Desfigurado, irreconhecível até pra mãe
Mãe, olha só que legal, carro que eu ganhei no natal
Tu que me deu, disse: Cuidado pra que não arranhe
Menino doido, tu quebrou até os friso
Tem noção do prejuízo?
Acho que o teu véio vai te matar
Os olhos dele esperando o carro do ano
Um modelo italiano
Que acabaram de inventar

Carrão da porra, tu pisava, ele voava
Tu freava, ele ancorava
E eu lá dentro a me debater
No bate-bate com a cabeça no volante
Voei pelo vidro da frente
A raiva preta eu não pude conter

Com o sangue quente
Cortei a testa
Quebrei os dente
E toda aquela gente
Peste, num vem ninguém me ajudar
Nem se mexiam, pior que isso, eles riam
Teto preto, o tempo fecha, os ovo inflama
Hora do pau cantar

Eu quero é ver o oco
Só na mãozada eu deitei seis, mas detestei matar
Eu quero é ver o oco
Sem controle, tocando fole, é hora de dançar

Meu ódio por automotores começou cedo
Depois que eu tranquei os dedo na porta dum Opalão
Meu pai de dentro se ria que se mijava
Achou que o filho festejava, era dia de Cosme e Damião
Depois do dedo, foi o braço, a perna, as costa
Tu duvida, bate aposta
Pois muitos vão lhe testemunhar
Tanta fratura que deixa a doutora louca
É pino até no céu da boca
Tu cansa só de tentar contar

Eu quero é ver o oco
É pedir muito uma enfermeira vir me ajudar?
Eu quero é ver o oco
Ó enfermeira, gente boa, vem me medicar

Eu quero é ver o oco
Eu quero é ver o oco."""

contador = 0

for letra in musica:
    if letra.lower() == 'a':
        contador += 1


qnt_palavras = musica.split()

letras = 0 
for c in musica:
    if c != " ":
        letras += 1
    
print ("A quantidade de letras na muscica eh: ", letras)
print ("A quantidade de de palvras na musica eh: ", len(qnt_palavras))
print ("A quantidade de letras 'a' na musica eh: ", contador)
