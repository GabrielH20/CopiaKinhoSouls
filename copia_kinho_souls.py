import math
from random import choice
import random

linha = '-'*30

def opcao_continuar(classe,nome):
    input(f'Sir {nome}, grande {classe}, aperte para continuar:')
    return None

#Seleção de personagens
while True:

    print(linha)
    print('Bem Vindo a Cópia do Kinho Souls\nEscolha sua Classe!') #https://github.com/HerickReis/KINHO-SOULS
    print(linha)
    print(f'Classes:\n{linha}\n[1] - Guerreiro\n[2] - Mago\n[3] - Samurai\n[4] - Barbaro\n{linha}')
    menu_de_personagem = int(input('Escolha seu personagem: '))
    print(linha)

    lista_de_classes = ['Guerreiro','Mago','Samurai','Barbaro']
    if menu_de_personagem in [1,2,3,4]:
        classe_personagem = lista_de_classes[menu_de_personagem-1]
        print(f'A classe do seu personagem é : {classe_personagem}\n{linha}')
        nome_do_jogador = input('Digite aqui o nome da sua escolha caro herói: ')
    else:
        print('Infelizmente você digitou um valor inválido!\nTente Novamente')
        continue
    opcao_continuar(classe_personagem,nome_do_jogador)
    break

#Status de cada Classe

print(linha)
visualizar_status = input(f'Deseja ver os benefícios da sua classe, nobre {nome_do_jogador}? [S] ou [N]').lower().startswith('s')
print(linha)

Lista_status_classes =[
    {'Nome Da Classe':'Guerreiro','Resistência a Dano Físico':40,'Resistência a Dano Mágico':10,'Poder de Ataque':20},

    {'Nome Da Classe':'Mago','Resistência a Dano Físico':10,'Resistência a Dano Mágico':60,'Poder de Ataque':20},

    {'Nome Da Classe':'Samurai','Resistência a Dano Físico':21,'Resistência a Dano Mágico':14,'Poder de Ataque':20},

    {'Nome Da Classe':'Barbaro','Resistência a Dano Físico':40,'Resistência a Dano Mágico':5,'Poder de Ataque':30}
]

status_player = []
def status():
    print(linha)
    for item in Lista_status_classes:
        if item['Nome Da Classe']==classe_personagem:   
            for chave,valor in item.items():
                print(f'{chave} : {valor}')
                if valor not in lista_de_classes:
                    status_player.append(valor)
if visualizar_status is True:
    print('Veja seus status:')
else:
    print('Vai ver mesmo assim que to com preguiça de pensar em uma maneira de colocar seus status em variáveis de outra maneira')
status()
opcao_continuar(classe_personagem,nome_do_jogador)
print(f'{status_player=}')

#Sorteando Obstáculos

caminhos = ["Penhasco", "Caminho vazio", "Buraco",'Desfiladeiro Ingrime','Campo da Morte','Show da Mc Pipokinha','Mundo Dos Cogumelos']
lugares_exploraveis = ['Casa Abandonada','Toca de Coelho','Bar de Maluco','Mansão Dessombrada','Porão de uma Waifu','Casa da Boqueteira do Faria lima']
inimigo = ["Inimigo Forte" , "Inimigo Fraco",'UM RALUCA CHAMANDO CALL NO DISCORD']
opcoes_para_encontrar = ['Coelhinhos','Mâios de Velhos fofos','Comida Semi Estragada','Um girino dourado','Sua mãe','o sentido da vida']

def aleatorizar_escolha(lista_opcoes):
    opcao = choice(lista_opcoes)
    return opcao
print(linha)

def criar_obstaculo_caminho(caminhos):
    
    print(f'{linha}\nO nobre {nome_do_jogador} estava andando em um {aleatorizar_escolha(caminhos)}, sem destino e com medo de tudo,')
    while True:
        direcao = input(f'Lá encontrou uma bifurcação, e ponderou se seguria pela:\n[E] - Esquerda\n[D] - Direita\nDigite aqui:').lower()
        print(linha)
        if direcao not in ['e','d']:
            print(f'Infelizmente você se perdeu e se encontrou novamente no mesmo local!\n{linha}')
            continue
        else:
            if direcao=='d':
                print('Vc saiu dessa floresta e encontra UM INIMIGO!')
                break
            else:
                print(f'Vc vai pelo caminho da Esquerda e encontra um(a) {aleatorizar_escolha(lugares_exploraveis)}')
                entrar_exploracao = input('Deseja Explorar o Local?\n[S] - sim\n[N] - não\nDigite aqui a Resposta:').lower()
                print(linha)
                if entrar_exploracao not in ['s','n']:
                    print(f'Digitou errado, volte toda a exploração!')
                elif entrar_exploracao=='s':
                    print(f'Lá você vasculha todo o local em busca de tesouros como o(a) {aleatorizar_escolha(opcoes_para_encontrar)}mas encontra UM INIMIGO')
                    break
                elif entrar_exploracao=='n':
                    print(f'Tnc tome um inimigo pra parar de ser covarde!')
                    break
vitoria = 0 
def criar_obstaculo_inimigo(inimigo):
    global vitoria
    print(f'Vc encontrou um {aleatorizar_escolha(inimigo)}\n{linha}')

    vida_player = 10
    vida_inimigo = 10
    dano_inimigo = random.randint(10,30)

    resistencia_fisica,resistencia_magiaca,dano_jogador = status_player
    while True:
        acao_combate = int(input(f'Escolha a Ação que deseja tomar:\n[1] - Atacar\n[2] - Defender\nDigite aqui o que deseja:'))
        print(linha)

        #calcular resistencia do jogador
        dano_sofrido = dano_inimigo - (dano_inimigo - (dano_inimigo * resistencia_fisica/100 ))
        dano_sofrido_inimigo = dano_jogador - (dano_jogador - (dano_jogador*30/100)) #Falha no código todos tem a mesma resistência fiquei com preguiça :p
        
        acao_inimigo = choice(['Defender','Atacar'])
        if acao_combate not in [1,2]:
            print('Tente novamente')
            continue
    
        if acao_combate==2:
            if acao_combate=='Defender':
                print('Ambos defenderam e nada rolou')
                continue
            else:
                print(f'O inimigo atacou e deu {dano_sofrido}')
        else:
            if acao_inimigo=='Atacar':
                print(f'Tanto player quanto inimigo atacaram e deram, respectivamente, {dano_inimigo} e {dano_jogador}')
            else:
                print(f'Só você atacou,enquanto o inimigo defendeu,mas conseguiu penetrar um pouco da defesa e deu 2 de dano')
                vida_inimigo-=2
        vida_player-=dano_sofrido
        vida_inimigo-=dano_jogador
        print(f'Sua vida:{vida_player:.2f}\nVida Inimigo:{vida_inimigo:.2f}')
        opcao_continuar(classe_personagem,nome_do_jogador)
        print(linha)
        if vida_inimigo<=0:
            print('Parabéns vc ganhou!')
            vitoria+=1
            break
        if vida_player<=0:
            print('Franginho mas continue mesmo assim!')
            break
        print(linha)

while True:
    if vitoria!=2:
        criar_obstaculo_caminho(caminhos)
        print(linha)
        criar_obstaculo_inimigo(inimigo)
        opcao_continuar(classe_personagem,nome_do_jogador)
    else:
        print(linha)
        print('Parabéns vc finalizou essaa cópia de jogo do meu inscrito pol4r285, espero que tenha gostado :)')
        print('Me serviu de aprendizado tanto para a prática de funções,lista e dicionários')
        print('Como analisar outros códigos, além de mostrar a evolução que tive para práticas melhores')
        print('Seu código ficou muito bom! Não teria consegui fazer o meu vídeo apenas com if, mas vc foi e tentou e isso é admirável pra caralho')
        opcao_continuar(classe_personagem,nome_do_jogador)


            
