class Pokemon:
    def __init__(self, altura, velocidade, peso, ataque, defesa, id, nome):
        self.__altura = float(altura)
        self.__velocidade = float(velocidade)
        self.__peso = float(peso)
        self.__ataque = float(ataque)
        self.__defesa = float(defesa)
        self.__id = int(id)
        self.__nome = str(nome)


    @property
    def altura(self):
        return self.__altura

    @property
    def velocidade(self):
        return self.__velocidade

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
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

