class Pokemon:
    def __init__(self, id, nome, altura, peso, ataque, defesa, velocidade):
        self.__id = str(id)
        self.__nome = str(nome)
        self.__altura = float(altura)
        self.__peso = float(peso)
        self.__ataque = int(ataque)
        self.__defesa = int(defesa)
        self.__velocidade = int(velocidade)


    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def altura(self):
        return self.__altura

    @property
    def peso(self):
        return self.__peso

    @property
    def ataque(self):
        return self.__ataque 

    @property
    def defesa(self):
        return self.__defesa

    @property
    def velocidade(self):
        return self.__velocidade

