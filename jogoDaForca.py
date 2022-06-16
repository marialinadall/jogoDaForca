import os 
from assets.main2 import limparTela, dicas, vencedor, perdedor
class bcolors:
    OK = '\033[92m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 

print("***********************************")
print("***BEM-VINDO(A) AO JOGO DA FORCA***")
print("***********************************")

desafiante = input("Digite o nome do desafiante: ")
competidor = input("Digite o nome do competidor: ")
limparTela()

n = ["0", "1"]
letras_escolhidas = [] 
chances = 5
tentativas = 0 
dica = 0
faltam = 2
letras_validas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

palavra = input("Ao desafiante, digite sua palavra-chave para o jogo da Forca: ")
palavras = list(palavra)
letras = palavra
if letras not in letras_validas:
    print("Esse caractere não é válido! Tente uma letra da próxima vez!")
limparTela()

def desafianteVencedor ():
    print("Você,", desafiante, ",venceu o JOGO DA FORCA!")
    print("O(A) competidor(a),", competidor, ",perdeu :(")
    print("\nA palavra era:", palavra)

def competidorVencedor ():
    print("Você,", competidor, ",venceu o JOGO DA FORCA!")
    print("O(A) Desafiante,", desafiante,",perdeu :(")
    print("A palavra era:", palavra)

arquivo = open ("jogo.forca", "w")
arquivo.write (desafiante)
arquivo.write ("\n")
arquivo.write(competidor)
arquivo.write ("\n")
arquivo.write (palavra)
arquivo.write ("\n")
arquivo.close 

arquivo = open ("jogo.forca", "r")
letras = len(palavra)
print ("Número de letras na palavra: ",letras)
lista_Dicas2 = dicas()
limparTela()

estado_atual = len(palavra) * ["*"]
print("Aqui é como está até agora: ", estado_atual)

try:
    
    while True:
        jogar = input("\nVocê deseja Jogar [0] ou Solicitar uma dica [1]? ")
        limparTela()

        if jogar == "1":
            faltam = faltam - dica 
            dica = dica + 1
            print ("A sua dica é: ", lista_Dicas2.pop(), "\nVocê já pediu", dica, "dica(s), agora restam", faltam, "dicas!")
            print("\nAgora você tem que chutar uma letra!")
            faltam = 2
            chute = input("Informe a letra que deseja arriscar: ")
            letras_escolhidas.append(chute.upper())

            if chute not in letras_validas:
                    print("Esse caractere não é válido! Tente uma letra da próxima vez")

            if chute in palavra:
                print( bcolors.OK + "Parabéns, você acertou a letra!" + bcolors.RESET)
                for i in range(len(palavra)):
                        if chute == palavra[i]:
                            estado_atual[i] = chute
                            print("\nAqui é como está até agora: ", estado_atual)
                            print("\nAqui são as letras que já foram: ",(letras_escolhidas))
                            letras_escolhidas.append(chute.upper())
                            
            else:
                    print(bcolors.FAIL + "\nQue pena! Essa letra não está na palavra" + bcolors.RESET) 
                    tentativas = tentativas + 1
                    restam = (chances - tentativas)
                    print("Você já errou", tentativas, "vez(es), lhe restam",restam,"tentativa(s).")
                    print("\nAqui é como está até agora: ", estado_atual)
                    print("\nAqui são as letras que já foram: ",(letras_escolhidas))
                    letras_escolhidas.append(chute.upper())

        elif jogar == "0":
            chute = input("Informe a letra que deseja arriscar: ")
            letras_escolhidas.append(chute.upper())

            if chute not in letras_validas:
                    print("Esse caractere não é válido! Tente uma letra da próxima vez!")

            if chute in palavra:
                print( bcolors.OK + "Parabéns, você acertou a letra!" + bcolors.RESET)
                for i in range(len(palavra)):
                        if chute == palavra[i]:
                            estado_atual[i] = chute
                            print("Aqui é como está até agora: ", estado_atual)
                            print("\nAqui são as letras que já foram: ",(letras_escolhidas))
                            letras_escolhidas.append(chute.upper())
                            
            else:
                    print(bcolors.FAIL + "\nQue pena! Essa letra não está na palavra" + bcolors.RESET) 
                    tentativas = tentativas + 1
                    restam = (chances - tentativas)
                    print("Você já fez", tentativas, "tentativa(s), lhe restam",restam,"tentativa(s).")
                    print("\nAqui é como está até agora: ", estado_atual)
                    print("\nAqui são as letras que já foram: ",(letras_escolhidas))
                    letras_escolhidas.append(chute.upper())
        else:
            print("Comando invalido")
            jogar == 1            

        if tentativas == 5:
            print("O Jogador:",competidor,"perdeu! Nessa partida o vencedor é o(a) Desafiante:",desafiante)
            perdedor() 
            desafianteVencedor() 
            break

        elif estado_atual == palavras:
            vencedor()
            competidorVencedor()
            break
        
except:
    if chute not in letras_validas and jogar not in n:
        print("Esse caractere não é válido! Tente novamente!")
        limparTela()
