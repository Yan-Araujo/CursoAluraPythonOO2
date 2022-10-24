class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def dar_like(self):
        self.__likes += 1

    def exibir_dados(self):
        print(f"Filme: {self.__nome}, Ano: {self.ano}, Duração: {self.duracao}")


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def exibir_dados(self):
        print(f"Série: {self.__nome}, Ano: {self.ano}, Temporadas: {self.temporadas}")


filme1 = Filme("Vingadores", 2010, 240)
serie1 = Serie("One Piece", 1995, 17)

Filme.exibir_dados(filme1)
Serie.exibir_dados(serie1)

