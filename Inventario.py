import pickle

Nome = ''
Inventario = []

def Criar_Inventario():


    # Pergunta qual o nome do personagem para comparar depos
    Nome = input("QUal o nome do seu personagem?")
    Sender_ID = "Jorge"
    # Abre e fecha o arquivo do jeito "pytonico"
    with open(f"Inventario/{Nome}.pickle", "wb") as Inv:
        
        Inventario.append(Sender_ID)
        pickle.dump(Inventario, Inv)

    print("Inventario criado!")


def Mostrar_Inventario():

    # Pergunta qual o nome do personagem para comparardepois
    Nome = input("Qual inventario você deseja abrir?")


    # É necessario abrir desse jeito para que possamos usar as variaves fora do WITH
    Abrir_Inv = open(f"Inventario/{Nome}.pickle", "rb")
    Ler_Inv = pickle.load(Abrir_Inv)

    # Passa por cada item do inventario retornando cada iteravel como o comando que demos
    for item in Ler_Inv:
        
        # Variavel contador que vai indicar a posicao de cada item
        # Pos = Posição
        Pos = 0
        
        print(f"{Pos}  :  {item}")
        
        # Adiciona 1 no nosso contador para que tenha sempe o mesmo numero da lista
        Pos += 1 


def Autualizar_inventario():

    # Booleano para quebrar o looping quando quisermos sair
    Sair = False

    

    # Variavel que vai receber nome para comparação
    Nome = input("Qual inventario você deseja atualizar?")

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
    if Sender_ID == Ler_Inv[0] : # or Sender_ID == "350364616657862679"  < -- Codigo para reconhecer o meu discord
        
        while Sair == False:
            
            Input_Item = input("Escreva o nome do item")
            
            # Comando para sair do inventario
            if Input_Item == "sair" or Input_Item == "Sair" or Input_Item == "SAIR":
                break
            

            # Se sair não for ativado começam as etapas de salvar os novos itens no inventario
            else : 

                # Adiciona o item digitado pelo usuario na lista " ITEM "
                Item.append(Input_Item)
                
                # Mostra os parametros // serve apenas para configuração 
                print("printando item = ", Item)
                
                Abrir_Para_Escrita = open(f"Inventario/{Nome}.pickle", 'wb')
                pickle.dump(Item, Abrir_Para_Escrita)
                Abrir_Para_Escrita.close()
                
                print("printando arquivo ", Ler_Inv)


    else:
        pass

Criar_Inventario()
Autualizar_inventario()