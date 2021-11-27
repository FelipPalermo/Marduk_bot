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

    Alterar_Inv = input("Deseja alterar algo no inventario?")

    if Alterar_Inv == "sim" or Alterar_Inv == "Sim" or Alterar_Inv == "SIM":

# --------------------------------------------------------------------------------------------------------------
    
        # Booleano para quebrar o looping quando quisermos sair
        Sair = False

        if Nome != '':
            # Variavel que vai receber nome para comparação
            Nome = input("Qual inventario você deseja atualizar?")

        else:
            pass

        print(Nome)
        #Abrir arquivo para leitura
        Abrir_Inv = open(f"Inventario/{Nome}.pickle", "rb")
        Ler_Inv = pickle.load(Abrir_Inv)

        # Lista que vai receber os itens que vamos adicionar depois
        Item = [Ler_Inv]


        # Sender_ID vai servir para só o dono do inventario poder alteralo 
        Sender_ID = "Jorge" # Yamo altera essa string pra um comando que recebe o ID do usuario 

        # Se o sender ID for o mesmo que o primeiro parametro " QUE NO CASO SERA O ID"
        # if vai ser ativado, nos botando em um looping onde adicionaremos os itens
        if Ler_Inv[0] == Sender_ID : # or Sender_ID == "350364616657862679"  < -- Codigo para reconhecer o meu discord
            
            Abrir_Inv.close

            while Sair == False:
                
                Input_Item = input("Escreva o nome do item")
                
                # Comando para sair do inventario
                if Input_Item == "sair" or Input_Item == "Sair" or Input_Item == "SAIR" or Input_Item == "sair do inventario" : 
                    break


                

                # Sair do loop caso o player digite sair
                else: 

                    # Adiciona o item digitado pelo usuario na lista " ITEM "
                    Item.append(Input_Item)
                    
                    # Mostra os parametros // serve apenas para configuração 
                    print("printando item = ", Item)

                    with open(f"Inventario/{Nome}.pickle", "wb") as EF: 
                        pickle.dump(Item, EF)

                    with open(f"Inventario/{Nome}.pickle", 'rb') as RF:
                        Ler_INV1 = pickle.load(RF)
                        print("Printando arquivo", Ler_INV1)
                    
        else:
            pass

Inventario()