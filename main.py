import desenhos as d

palavra = input('Digite uma palavra secreta: ').lower().strip() #lower e para deixar tudo minusculo e strip e para tirar os espaçamentos

for x in range(50):
    print()

digitadas = []
acertos   = []
erros     = 0

while True:
    
    adivinha = d.imprimir_palavra_secreta(palavra, acertos)

    # * CONDIÇÃO DE VITORIA
    if adivinha == palavra:
        print('Você acertou!')
        break
     
    # * TENTATIVAS
    tentativa = input('\nDigite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('Você já usou essa letra')
        continue
    else: 
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')
    

    d.desenhar_forca(erros)
    
    # * CONDIÇÃO DE FIM DE JOGO 
    if erros == 6:
        print('Gamer Over!')
        print(f'Apalavra correta era {palavra}.')
        break    