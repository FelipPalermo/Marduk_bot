import pickle

def Remover_Do_Inventario():

    # Booleano para quebrar o looping quando quisermos sair
    Sair = False

    # Variavel que vai receber nome para comparação
    Nome = input("Qual inventario você deseja atualizar?")

    #Abrir arquivo para leitura
    Abrir_Inv = open(f"Inventario/{Nome}.pickle", "rb")
    Ler_Inv = pickle.load(Abrir_Inv)

    # Lista que vai receber os itens que vamos adicionar depois
    Item = Ler_Inv

    # ID para comparacao
    Ler_ID = Ler_Inv


    # Sender_ID vai servir para só o dono do inventario poder alteralo 
    Sender_ID = "Jorge" # Yamo altera essa string pra um comando que recebe o ID do usuario 


    # Se o sender ID for o mesmo que o primeiro parametro " QUE NO CASO SERA O ID"
    # if vai ser ativado, nos botando em um looping onde adicionaremos os itens
    if Ler_ID[0] == Sender_ID: # or Sender_ID == "350364616657862679"  < -- Codigo para reconhecer o meu discord

        while Sair == False:
            
            # Posicao no inventario 
            Item_Pos = 0

            # Tamanho do inventario
            Inv_Len = len(Ler_Inv)

            # Mostra todos os itens no inventario selecionado            
            for item in Ler_Inv:

                Item_Pos += 1
                
                print(f"{Item_Pos} : {Ler_Inv[Item_Pos]}")
                
                if Item_Pos >= Inv_Len - 1 :
                    break
            
            try :
                # Recebe o numero do item + 1 porque excluimos o index 0 no começo
                Input_Item = input("Escreva o nome completo do item, ou sair")

                # Comando para sair do inventario
                if Input_Item == "sair" or Input_Item == "Sair" or Input_Item == "SAIR" or Input_Item == "sair do inventario" : 
                    break

                
                else:
                
                    # Remove o item digitado pelo usuario na lista " ITEM "
                    Item.remove(Input_Item)
                    
                    # Mostra os parametros // serve apenas para configuração 
                    print("printando item = ", Item)

                    with open(f"Inventario/{Nome}.pickle", "wb") as EF: 
                        pickle.dump(Item, EF)

                    with open(f"Inventario/{Nome}.pickle", 'rb') as RF:
                        Ler_INV1 = pickle.load(RF)
                        print("Printando arquivo", Ler_INV1)
            
            except : 
                print("Você digitou algo errado!")
                
    else:
        pass




Remover_Do_Inventario()