import pickle


def Inventario():

    # Pergunta qual o nome do personagem para comparardepois
    Nome = input("Qual inventario você deseja abrir?")


    # É necessario abrir desse jeito para que possamos usar as variaves fora do WITH
    Abrir_Inv = open(f"Inventario/{Nome}.pickle", "rb")
    Ler_Inv = pickle.load(Abrir_Inv)


    # Variavel contador que vai indicar a posicao de cada item
    # Inv_Pos = Posição no inventario
    Inv_Pos = 0


    # Guarda o tamanho do inventario como int para compararmos depois
    Inv_len = len(Ler_Inv)


    # Passa por cada item do inventario retornando cada iteravel como o comando que demos
    for item in Ler_Inv:
        
        # Adiciona 1 no nosso contador para que tenha sempe o mesmo numero da lista
        Inv_Pos += 1 

        # Mostra a posição no iventario e o item, excluindo o ID do jogador
        print(f"{Inv_Pos}  :  {Ler_Inv[Inv_Pos]}")


        # Quebra o loop caso a posição no inventario seja maior que o tamanho do inventario -1 
        if Inv_Pos >= Inv_len - 1 :
            break


Inventario()