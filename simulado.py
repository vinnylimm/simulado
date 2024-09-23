gabarito=input("cole o gabarito aqui: ")
#print("----------parte 1-------")
#print(gabarito)

gabarito=gabarito.replace(" ", "\n")
gabarito=gabarito.replace(".\n", " ")
#print("-----------parte 2---------")
#print(gabarito)
with open('gabarito.txt', 'w') as gab:
  gab.write(gabarito)

with open('gabarito.txt', 'r') as gab:
  gabarito=gab.readlines()

#print("-------------parte 3-----------")
#print(gabarito[0])

with open('respostas.txt', 'r') as respostas:
  respostas=respostas.readlines()

#print(len(respostas))
#respostas=" ".join(respostas)
#respostas=str(respostas)
#print(respostas[0])

#---------------------



with open('gabarito.txt', 'r') as gab:
    gabarito = gab.readlines()

with open('respostas.txt', 'r') as respostas:
    respostas = respostas.readlines()

resultado = []
acertos = 0
erros = 0

for cont in range(20):
    if "CERTO" in respostas[cont]:
        if "CERTO" in gabarito[cont]:
            resultado.append(f'{respostas[cont].strip()}----ACERTOU')
            acertos += 1
        else:
            resultado.append(f'{respostas[cont].strip()}----ERROU')
            erros += 1
    elif "ERRADO" in respostas[cont]:
        if "ERRADO" in gabarito[cont]:
            resultado.append(f'{respostas[cont].strip()}----ACERTOU')
            acertos += 1
        else:
            resultado.append(f'{respostas[cont].strip()}----ERROU')
            erros += 1
    elif " A" in respostas[cont]:
        if " A" in gabarito[cont]:
            resultado.append(f'{respostas[cont].strip()}----ACERTOU')
            acertos += 1
        else:
            resultado.append(f'{respostas[cont].strip()}----ERROU')
            erros += 1
    elif " B" in respostas[cont]:
        if " B" in gabarito[cont]:
            resultado.append(f'{respostas[cont].strip()}----ACERTOU')
            acertos += 1
        else:
            resultado.append(f'{respostas[cont].strip()}----ERROU')
            erros += 1
    elif " C" in respostas[cont]:
        if " C" in gabarito[cont]:
            resultado.append(f'{respostas[cont].strip()}----ACERTOU')
            acertos += 1
        else:
            resultado.append(f'{respostas[cont].strip()}----ERROU')
            erros += 1
    elif " D" in respostas[cont]:
        if " D" in gabarito[cont]:
            resultado.append(f'{respostas[cont].strip()}----ACERTOU')
            acertos += 1
        else:
            resultado.append(f'{respostas[cont].strip()}----ERROU')
            erros += 1
    elif " E" in respostas[cont]:
        if " E" in gabarito[cont]:
            resultado.append(f'{respostas[cont].strip()}----ACERTOU')
            acertos += 1
        else:
            resultado.append(f'{respostas[cont].strip()}----ERROU')
            erros +=1
resultado=" ".join(resultado)
resultado=str(resultado)
resultado=resultado.replace("----ACERTOU", "----ACERTOU\n")
resultado=resultado.replace("----ERROU","----ERROU\n")
print(resultado)
print(f"Acertos: {acertos}")
print(f"Erros: {erros}")
