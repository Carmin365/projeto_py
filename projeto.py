numero_oculto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas):
    print('Tentativa{} de {}' .format(rodada, total_de_tentativas))

    chute = int(input('Digite o seu número: '))
    print('Você digitou: ', chute)

    acertou = numero_oculto == chute
    maior = chute > numero_oculto
    menor = chute < numero_oculto

    if (acertou):
        print('Você acertou!')
        break
    elif (maior):
        print('Você errou! O seu chute foi maior que o número oculto')
    elif (menor):
        print('Você errou! O seu chute foi menor que o número oculto')
        print('Fim do jogo!')