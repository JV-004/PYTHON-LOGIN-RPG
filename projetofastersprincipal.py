import getpass

class Netuno_rpg:
    def __init__(self):
        self.nome_jogador = None
        self.cor_olhos = None
        self.raça = None
        self.sexo = None
        self.cor_cabelo = None
        self.cor_pele = None
        self.nome_classe = None
        self.nome_montaria = None

    def tela_cadastro(self):
        print("\n==TELA DE CADASTRO==")
        self.nome_jogador = input("Nome: ")
        data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        dia, mes, ano = map(int, data_nascimento.split('/'))
        idade = 2023 - ano
        if idade < 18:
            print("DEVE TER NO MÍNIMO 18 ANOS PARA JOGAR.")
            return self.tela_cadastro()
        self.email = input("Digite seu email: ")
        self.senha = input("Digite a senha desejada: ")
        confirmar_senha = getpass.getpass("Confirme a senha: ")
        if self.senha != confirmar_senha:
            print("Senhas não coincidem. Tente novamente.")
            return self.tela_cadastro()

    def tela_login(self):
        print("\n==TELA DE LOGIN==")
        tentativas = 0
        max_tentativas = 3

        while tentativas < max_tentativas:
            email = input("Digite seu email: ")
            senha = getpass.getpass("Digite sua senha: ")

            if email.lower() == self.email.lower() and senha == self.senha:
                print("Login bem-sucedido! Direcionando para a tela do jogo...")
                break
            else:
                print("Email ou senha incorretos. Tente novamente.")
                tentativas += 1
                if tentativas >= max_tentativas:
                    print("TENTATIVAS ESGOTADAS, TENTE NOVAMENTE")
                    return self.tela_login()

    def exibir_opcoes(self, opcoes, mensagem):
        while True:
            for chave, valor in opcoes.items():
                print(f"{chave}) {valor}")
            escolha = input(mensagem)
            if escolha in opcoes:
                return opcoes[escolha]
            else:
                print("Escolha inválida. Tente novamente.")

    def customizacao(self):
        print("\n==TELA DE CUSTOMIZAÇÃO==")

        print("\n==ESCOLHA SUA RAÇA==")
        racas = {'1': 'Elfo [Agilidade e resistência a feitiço]',
                '2': 'Anão [Resistência a veneno e proficiência em machados]',
                '3': 'Humano [Proficiência em armas e boa capacidade de carga]',
                '4': 'Meio-elfo [Agilidade e destreza]',
                '5': 'Tiefiling [Resistência ao fogo e visão noturna até 12 metros]'}
        self.raça = self.exibir_opcoes(racas, "\nEscolha o número da raça desejada: ")

        print("\n==COR DE CABELO==")
        cores_cabelo = {'1': 'preto', '2': 'branco', '3': 'marrom'}
        self.cor_cabelo = self.exibir_opcoes(cores_cabelo, "\nDigite o número da cor do cabelo do seu avatar: ")

        print("\n==COR DA PELE==")
        cores_pele = {'1': 'branco', '2': 'preto', '3': 'pardo', '4': 'moreno'}
        self.cor_pele = self.exibir_opcoes(cores_pele, "\nDigite o número da cor da pele do seu avatar: ")

        print("\n==COR DOS OLHOS==")
        cores_olhos = {'1': 'castanhos', '2': 'preto', '3': 'verde', '4': 'azul'}
        self.cor_olhos = self.exibir_opcoes(cores_olhos, "\nDigite o número da cor do olho do seu avatar: ")

        print("\n==SEXO==")
        generos = {'1': 'masculino', '2': 'feminino'}
        self.sexo = self.exibir_opcoes(generos, "\nDigite o número do sexo do seu avatar: ")

        print("\n==CLASSE==")
        classes = {'1': 'Paladino. [Lança e escudo. Vida:85 ,Mana:55 , Velocidade de Ataque:20]',
                '2': 'Atirador. [Pistola e Canhão. Vida:50 ,Mana:55 , Velocidade de Ataque:85]',
                '3': 'Guerreiro. [Espada de uma mão e Escudo. Vida:75 ,Mana:80 , Velocidade de Ataque:35]',
                '4': 'Bárbaro. [Machado, Marreta e Espada de duas mãos. Vida:75 ,Mana:95 , Velocidade de Ataque:40]',
                '5': 'Arqueiro. [Arco. Vida:45 ,Mana:60 , Velocidade de Ataque:75]',
                '6': 'Bardo. [Alaúde, canto. Vida:40 , Mana:90 , Velocidade de Ataque:35]'}
        self.nome_classe = self.exibir_opcoes(classes, "\nDigite o número da classe do seu avatar: ")

        print("\n==MONTARIA==")
        montarias = {'1': 'Cavalo[vida: 130, velocidade: 5m/s, descanso: 5 minutos]',
                    '2': 'Lobo infernal[vida: 110, velocidade: 8m/s, descanso: 4 minutos]',
                    '3': 'Pantera negra[vida: 145, velocidade: 7m/s, descanso: 3 minutos]',
                    '4': 'Tigre das neves[vida: 160,  velocidade: 6m/s, descanso: 6 minutos]',
                    '5': 'Dragão das trevas[vida: 200,  velocidade: 10m/s, descanso: Nenhum]'}
        self.nome_montaria = self.exibir_opcoes(montarias, "\nDigite o número da montaria do seu avatar: ")

        print("\n==SEU PERSONAGEM FINAL==")
        print("Sua raça é: ", self.raça)
        print("Cor da pele: ", self.cor_pele)
        print("Cor do cabelo: ", self.cor_cabelo)
        print("Cor dos olhos: ", self.cor_olhos)
        print("Gênero: ", self.sexo)
        print("Sua classe: ", self.nome_classe)
        print("Sua montaria: ", self.nome_montaria)

        while True:
            resposta = input("\nDeseja prosseguir? (Sim/Não): ").capitalize()
            if resposta == "Sim":
                print("\nCarregando Netuno RPG...")
                break
            elif resposta == "Não":
                self.customizacao()
            else:
                print("\nOpção inválida, sim ou não")



netuno_rpg = Netuno_rpg()
netuno_rpg.tela_cadastro()
netuno_rpg.tela_login()
netuno_rpg.customizacao()