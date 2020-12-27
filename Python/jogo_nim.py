
def partida():
    pecas_limite = int(input("Quantas peças? "))
    limite_pecas_jogada = int(input("Limite de peças por jogada? "))
    if (limite_pecas_jogada > pecas_limite) or (pecas_limite < 1) or (limite_pecas_jogada < 1):
        print("Oops! Jogada inválida! Tente de novo.")
        return partida()
    jogada_computador = False
    if pecas_limite % (limite_pecas_jogada + 1) == 0:
        print("\nVocê começa!")
    else:
        print("\nComputador começa!")
        jogada_computador = True
    while pecas_limite > 0:
        if jogada_computador:
            valor = computador_escolhe_jogada(pecas_limite, limite_pecas_jogada)
            pecas_limite = pecas_limite - valor
            if valor == 1:
                print("\nO computador tirou uma peça")
            else:
                print("\nO computador tirou", valor, "peças")
            jogada_computador = False
        else:
            valor = usuario_escolhe_jogada(pecas_limite, limite_pecas_jogada)
            pecas_limite = pecas_limite - valor
            if valor == 1:
                print("\nVoce tirou uma peça")
            else:
                print("\nVocê tirou", valor, "peças")
            jogada_computador = True
        if pecas_limite == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            if pecas_limite != 0:
                print("Agora restam,", pecas_limite, "peças no tabuleiro.\n")
    print("Fim do jogo! O computador ganhou!")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    jogo = int(input("2 - para jogar um campeonato\n> "))
    if jogo == 1:
        print("")
        partida()
    else:
        if jogo == 2:
            print("\nVoce escolheu um campeonato!\n")
            campeonato()


def usuario_escolhe_jogada(pecas_limite, limite_pecas_jogada):
    jogada = True
    while pecas_limite >= limite_pecas_jogada and jogada:
        valor = int(input("Quantas peças você vai tirar? "))
        if valor > limite_pecas_jogada or valor < 1:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        else:
            jogada = False
    return valor


def computador_escolhe_jogada(pecas_limite, limite_pecas_jogada):
    valor = 1
    while valor != limite_pecas_jogada:
        if (pecas_limite - valor) % (limite_pecas_jogada + 1) == 0:
            return valor
        else:
            valor += 1
    return valor


def campeonato():
    rodada = 1
    while rodada <= 3:
        print("\n**** Rodada", rodada, "****\n")
        partida()
        rodada = rodada + 1
    print("\nPlacar: Você 0 X 3 Computador")


if __name__ == "__main__":
    main()