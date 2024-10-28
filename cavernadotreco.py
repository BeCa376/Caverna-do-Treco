import random

# Singleton: Mapa do Jogo
class MapaJogo:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(MapaJogo, cls).__new__(cls)
        return cls._instancia

    def __init__(self):
        self.cenarios = ["Entrada da Caverna", "Caverna"]  # Cenários limitados
        self.cenario_atual = self.cenarios[0]  # Cenário inicial

    def mudar_cenario(self, novo_cenario):
        if novo_cenario in self.cenarios:
            self.cenario_atual = novo_cenario
            print(f"Cenário alterado para: {novo_cenario}")

# State: Estados do Personagem
class EstadoPersonagem:
    def acao(self):
        raise NotImplementedError

class Vivo(EstadoPersonagem):
    def acao(self):
        return "O personagem está vivo e pronto para lutar!"

class Ferido(EstadoPersonagem):
    def acao(self):
        return "O personagem está ferido, mas ainda pode lutar."

class Morto(EstadoPersonagem):
    def acao(self):
        return "O personagem está morto e não pode mais lutar."

class Personagem:
    def __init__(self, nome, carater, raca, forca, agilidade, magia):
        self.nome = nome
        self.estado = Vivo()  # O estado inicial é vivo
        self.carater = carater
        self.raca = raca  # Novo atributo para raça
        self.forca = forca
        self.agilidade = agilidade
        self.magia = magia

    def mudar_estado(self, novo_estado):
        self.estado = novo_estado

    def agir(self):
        return self.estado.acao()

    def status(self):
        return (f"{self.nome}: {self.carater} {self.raca} Força {self.forca}, Agilidade {self.agilidade}, "
                f"Magia {self.magia}")

class Goblin:
    def __init__(self):
        self.nome = "Goblin"
        self.carater = "Goblin"
        self.forca = 10
        self.agilidade = 10
        self.magia = 10
        self.estado = Vivo()  # Estado inicial é vivo

    def mudar_estado(self, novo_estado):
        self.estado = novo_estado

    def agir(self):
        return self.estado.acao()

    def status(self):
        estado_str = self.estado.acao()
        return (f"{self.nome} [{estado_str}]: {self.carater} Força {self.forca}, "
                f"Agilidade {self.agilidade}, Magia {self.magia}")
    
# Decorator: Atributos e Perícias
class DecoratorPersonagem(Personagem):
    def __init__(self, personagem):
        self.personagem = personagem

    def status(self):
        return self.personagem.status()

class ForcaExtra(DecoratorPersonagem):
    def status(self):
        self.personagem.forca += 5
        return super().status() + " (Força extra)"

class AgilidadeExtra(DecoratorPersonagem):
    def status(self):
        self.personagem.agilidade += 3
        return super().status() + " (Agilidade extra)"

class MagiaExtra(DecoratorPersonagem):
    def status(self):
        self.personagem.magia += 7
        return super().status() + " (Magia extra)"

# Função para criar personagens com atributos específicos
def criar_personagem(nome, carater, raca, forca, agilidade, magia):
    return Personagem(nome, carater, raca, forca, agilidade, magia)

def escolha_inicial():
    print()
    print("Opções:")
    print("1. Se esconder")
    print("2. Enfrentar")
    print()

def escolha_inicial2():
    if personagem_jogador.agilidade > goblin.agilidade:
        print("Você se escondeu do Goblin")
        print("Gostaria de atacar? (1. Sim)")
        escolha = int(input())
        print()

    elif personagem_jogador.agilidade < goblin.agilidade:
        print("O Goblin viu você e está pronto para o ataque.")
        print()
        escolha_inicial3()
        print()
        
    else:  # igualdade de força
        print("O Goblin não te viu, mas está desconfiado.")
        print("Gostaria de atacar? (1. Sim)")
        escolha = int(input())
        print()

def escolha_inicial3():
    print("Como gostaria de atacar?")
    escolhainicial3 = int(input("1. Força / 2. Magia "))
    if escolhainicial3 == 1:
        print()
        print("ATACAAAR!")
        print()
        print("[efeito sonoro de soco]")
        print()
                
# Comparando a força do jogador com a força do goblin
        if personagem_jogador.forca > goblin.forca:
            print("Você causou dano ao Goblin!")
            print("O Goblin está ferido!")
            goblin.mudar_estado(Ferido())  # Altera o estado do Goblin para Ferido
        elif personagem_jogador.forca < goblin.forca:
            personagem_jogador.mudar_estado(Ferido())
            print("O Goblin aguentou a porrada e atacou você!")
            print("Você está ferido.")
        else:  # igualdade de força
            print("O ataque foi bloqueado!")
            print("Você e o Goblin estão vivos.")

    elif escolhainicial3 == 2:
        print()
        print("Você usou magia!")
        print()
        print("[efeito sonoro de plimplim]")
        print()
                
        # Comparando a magia do jogador com a magia do goblin
        if personagem_jogador.magia > goblin.magia:
            print("Você causou dano ao Goblin!")
            goblin.mudar_estado(Ferido())  # Altera o estado do Goblin para Ferido
        elif personagem_jogador.magia < goblin.magia:
            personagem_jogador.mudar_estado(Ferido())
            print("O Goblin resistiu e te atacou! Você está ferido.")
        else:  # igualdade de magia
            print("A magia não chegou no Goblin! Você e o Goblin estão vivos.")

def escolha_inicial4():
    print("Como gostaria de re-atacar?")
    escolhainicial4 = int(input("1. Força / 2. Magia "))
    if escolhainicial4 == 1:
        print()
        print("ATACAAAR!")
        print()
        print("[efeito sonoro de soco]")
        print()
    
        # Comparando a força do jogador com a força do goblin
        if personagem_jogador.forca > goblin.forca:
            print("Você causou dano ao Goblin!")
            if goblin.estado.__class__ == Ferido:  # Verifica se o goblin está ferido
                print("Agora ele está morto!")
                goblin.mudar_estado(Morto())  # Altera o estado do Goblin para Morto
                print()
                print("O goblin cai no chão ensanguentado. Ele olha para você e fala suas últimas palavras:")
                print()
                print("- Ug'hak m'gruush! Zog nar chuk'taar draakh!")
                print()
                print("Você pega o tesouro valioso e sai da caverna com uma grande vitória nos braços. Parabéns!")
                print()
                print("FIM DO JOGO...")
            else:
                goblin.mudar_estado(Ferido())  # Altera o estado do Goblin para Ferido
                print("O Goblin está ferido!")
        elif personagem_jogador.forca < goblin.forca:
            personagem_jogador.mudar_estado(Morto())
            print()
            print("O Goblin aguentou a porrada e atacou você! Agora você está morto e a missão acabou!")
            print()
            print("FIM DO JOGO...")
        else:  # igualdade de força
            print("O ataque foi bloqueado! Você e o Goblin estão vivos.")

    elif escolhainicial4 == 2:
        print()
        print("Você usou magia!")
        print()
        print("[efeito sonoro de plimplim]")
        print()
                    
        # Comparando a magia do jogador com a magia do goblin
        if personagem_jogador.magia > goblin.magia:
            print("Você causou dano ao Goblin!")
            if goblin.estado.__class__ == Ferido:  # Verifica se o goblin está ferido
                print("Agora ele está morto!")
                goblin.mudar_estado(Morto())  # Altera o estado do Goblin para Morto
                print()
                print("O goblin cai no chão magicamente ensanguentado. Ele olha para você e fala suas últimas palavras:")
                print()
                print("- Ug'hak m'gruush! Zog nar chuk'taar draakh!")
                print()
                print("Você pega o tesouro valioso e sai da caverna com uma grande vitória nos braços. Parabéns", personagem_jogador.status(), "!")
                print()
                print("FIM DO JOGO...")
            else:
                goblin.mudar_estado(Ferido())  # Altera o estado do Goblin para Ferido
                print("O Goblin está ferido!")
        elif personagem_jogador.magia < goblin.magia:
            personagem_jogador.mudar_estado(Morto())
            print()
            print("O Goblin resistiu e te atacou! Agora você está morto e a missão acabou!")
            print()
            print("FIM DO JOGO...")
        else:  # igualdade de magia
            print("A magia não chegou no Goblin! Você e o Goblin estão vivos.")
    
# Função para escolher um personagem
def escolher_personagem():
    print("Escolha seu personagem:")
    print("1. Camila: Bárbara - Meio Orc, Força: 15, Agilidade: 10, Magia: 5")
    print("2. Brenda: Ladina - Tiefling, Força: 13, Agilidade: 12, Magia: 5")
    print("3. Gustavo: Druida - Elfo, Força: 5, Agilidade: 10, Magia: 15")
    print()
    
    try:
        escolha1 = int(input("Digite o número do seu personagem: "))
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
        return escolher_personagem()  # Repetir a escolha

    if escolha1 == 1:
        return criar_personagem("Camila", "Bárbaro", "Meio Orc", 15, 10, 0)
    elif escolha1 == 2:
        return criar_personagem("Brenda", "Ladina", "Tiefling", 5, 15, 5)
    elif escolha1 == 3:
        return criar_personagem("Gustavo", "Druida", "Elfo", 5, 5, 15)
    else:
        print("Escolha inválida! Tente novamente.")
        return escolher_personagem()  # Repetir a escolha

# Função Principal para Rodar
if __name__ == "__main__":
    # Criando o mapa (Singleton)
    mapa = MapaJogo()

    # Escolher um personagem
    personagem_jogador = escolher_personagem()

    # Exibindo status do personagem escolhido
    print("\nVocê escolheu:")
    print(personagem_jogador.status())

    # Mudar o estado do personagem
    personagem_jogador.mudar_estado(Vivo())
    print(personagem_jogador.agir())

    # Exibir o cenário inicial
    print("Cenário inicial:", mapa.cenario_atual)
    print()

    # Iniciar Jogabilidade
    print("Você está procurando um tesouro muito valioso escondido dentro de uma caverna desconhecida")
    print()

    # Mudar de cenário para "Caverna"
    mapa.mudar_cenario("Caverna")  # Chama o método corretamente
    print()

    # Mensagem sobre a entrada na caverna
    print(f"{personagem_jogador.nome} está entrando na caverna escura até que se depara com um Goblin que está protegendo o grandioso tesouro.")

    # Criando o Goblin
    goblin = Goblin()
    print(f"Você encontrou um inimigo: {goblin.status()}")
    escolha_inicial()

    escolhainicial = int(input("O que você faz?"))
    print()

    if escolhainicial == 1:
        escolha_inicial2()

        if escolhainicial == 1:
            escolha_inicial3()

        else:
            print("Opção inválida")

    if escolhainicial == 2:
        escolha_inicial3()

    else:
        print("Opção inválida!")
    
    print()
    print("E o combate contiua!!")
    print()

    escolha_inicial4()