import random, os #random faz o sorteio e OS limpa o terminal sem apagar as informações anteriores


    #ESSAS COISINHAS SÃO PRA APAGAR A PALAVRA DO JOGADOR ANTERIOS
def limpar(): #def cria a função de limpar
    os.system("cls" if os.name == "nt" else "clear") #essa porrinha aqui faz o terminal se apagar
    #os system serve pra mandar comandos pro computador
    #"cls" é um comando pro windows limpar o terminal
    #"clear" faz isso pro mac/linux
    #SLA OQ SERIA NT    



palavra = input("Digite a palavra: ")

impostor = random.randint(1, 4) #isso vai fazer o sorteio de 1 a 4 e o numero do sorteado vai ser o impostor

for nhaaa in range(1, 5):
    limpar()
    input(f"Jogador {nhaaa}, pressione ENTER para ver sua informação")
    limpar()
    
    if nhaaa == impostor:
        print("Você é o IMPOSTOR! ")
    else:
        print("Você NÃO é o impostor!")
        print("Sua palavra é:", palavra)

    input("Pressione ENTER para passar para o próximo jogador...")

limpar()

print("O impostor era o jogador:", impostor)

