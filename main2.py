import time #importa o relógio 
import os #importa o sistema operacional

def limparTela() : #cria uma função personalizada
    os.system("cls")

def aguardando(segundos) :
    time.sleep(segundos)

def escreverTela(texto) :
    print(texto.upper())


def dicas():
    x=0
    lista_dica = []
    while(x < 3):
        dica = input("Digite uma dica sobre a palavra: ")  
        lista_dica.append(dica)
        x = x + 1
    return lista_dica

def vencedor(): 
    print("            ___         ")
    print("         '.=====.'      ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         .' '.          ")
    print("        '-------'       ") 
    print("         VENCEDOR       ")
    print("                        ")

def perdedor():


 print("    ___                                          ")
 print("    .'``.``.                                     ")
 print(" __/ (o) `, `.                                   ")
 print("'-=`,     ;   `.                                 ")
 print("       :      `-.                                ")
 print("    /    ';        `.                            ")
 print("   /      .'         `.                          ")
 print("  |     (      `.     `-.._                      ")
 print("         ` ` `.          `-.._                   ")
 print("    `.   ;`-.._ `-`._.-. `-._   `-._             ")
 print("       `..'     `-.```.  `-._ `-.._.'            ")
 print("         `--..__..-`--'      `-.,'               ")
 print("            `._)`/                               ")
 print("             /--(                                ")
 print("         -./,--'`-,                              ")
 print("       ,^--(                     você perdeu :)' ")
 print("       ,--' `-,                                  ")


 
 