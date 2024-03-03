def imprimir_palavra_secreta(palavra, acertos):
    adivinha = ""
    for letra in palavra:
        if letra in acertos:
            adivinha += letra
        else:
            adivinha += '#'
    print(f'ADIVINHE ({len(palavra)} letras): ')
    for letra in adivinha:
        print(f'{letra} ', end='')
    print()

    return adivinha

def desenhar_forca(erros):
    
    score = 1000
    
    print("X==:==")
    print("X  :  ")
    if erros >= 1:
        print('X  O ')
        score = 900
    else:
        print('X')
    
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
        score = 800
    elif erros == 3:
        linha2 = " /| "
        score = 600
    elif erros >= 4:
        linha2 = " /|\ "
        score = 400
    print(f"x{linha2}")
    
    linha3 = ""
    if erros == 5:
        linha3 = " / "
        score = 200
    elif erros >= 6:
        linha3 += " / \ "
        score = 0
    print(f"x{linha3}")
    
    print(f"x\n=======")
    
    return score