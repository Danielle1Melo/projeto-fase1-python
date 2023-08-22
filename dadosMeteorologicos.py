meses = [
    "Janeiro", 
    "Fevereiro",
    "Março", 
    "Abril", 
    "Maio", 
    "Junho", 
    "Julho", 
    "Agosto", 
    "Setembro", 
    "Outubro", 
    "Novembro", 
    "Dezembro"
    ]
# initialize array with 12 positions, each one for each month
temperaturas = [0] * 12
qtdMesesEscaldantes = 0
mesMaisEscaldante = 0
mediaAnual = 0

mesMenosEscaldante = 0

mesesJaInformados = []

contagemMes = 0
while True:
    if contagemMes > 11:
        break

    mes = int(input("Digite um número equivalente ao mês do ano: "))
    if mes < 1 or mes > 12:
        print("Mês inválido")
        continue
    
    jaInformado = False
    for mesInformado in mesesJaInformados:
        if mes == mesInformado:
            print(f"Mês de {meses[mes -1]} já informado")
            jaInformado = True
            break
    
    if jaInformado:
        continue
    tempMax = float(input("Informe a temperatura máxima do mês em ºC: "))
    if tempMax < -60 or tempMax > 50:
        print("Temperatura inválida")
        continue

    temperaturas[mes - 1] = tempMax
    contagemMes = contagemMes + 1
    mesesJaInformados.append(mes)

#Temperatura média máxima anual
mediaAnual = sum(temperaturas) / len(temperaturas)
print(f"Média anual: {mediaAnual}")

#Quantidade de meses escaldantes
mesesEscaldantes = []
for indice, temp in enumerate(temperaturas):
    if temp > 38:
        qtdMesesEscaldantes = qtdMesesEscaldantes + 1
        mesesEscaldantes.append(meses[indice])
print(f"Quantidade de meses escaldantes: {qtdMesesEscaldantes}, mês(s): {mesesEscaldantes}")


#Mês mais escaldante do ano
maiorTemperatura = temperaturas[0]
for indice, temp in enumerate(temperaturas):
    if temp > maiorTemperatura:
       maiorTemperatura = temp
       mesMaisEscaldante = indice

print(f"Mês com a temperatura mais escaldante: {meses[mesMaisEscaldante]}, com a temperatura de: {maiorTemperatura} ºC")

#Mês menos quente do ano
menorTemperatura = temperaturas[0]
for indice, temp in enumerate(temperaturas):
    if temp < menorTemperatura :
       menorTemperatura = temp
       mesMenosEscaldante = indice

print(f"Mês com a temperatura menos escaldante: {meses[mesMenosEscaldante]}, com a temperatura de: {menorTemperatura} ºC")






