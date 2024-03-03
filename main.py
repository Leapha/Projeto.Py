import jogo as j
def mostrar_menu():
    print("="*30)
    print(" " * 7 + "JOGO DA FORCA")
    print("="*30)
    print("\n1 - JOGAR")
    print("2 - SCORE")
    print("3 - SAIR\n")
    print("="*30)
    
    
while True:
    mostrar_menu()
    opcao  = int(input("Escolha uma opção (1/2/3): "))
    
    if opcao == 1:
        print('Iniciando o jogo...')
        j.jogar()
        input('Digite qual quer tecla para continuar...')
    
    elif  opcao == 2:
        print('Mostrar score!')
        
    elif opcao == 3: 
        print('Encerrando jogo')
        break
    
    else: 
        print('Opção inválida! Tente novamente.')