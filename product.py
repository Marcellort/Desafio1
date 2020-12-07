import categorias
class Produto:
    __id: int
    __nome: str
    __descricao: str
    __valor: float
    __categoria= list()
    __peso: float
    __largura: float
    __altura: float

    def set_nome(self)-> None:
        nome = input('Digite o nome do seu produto: ')
        self.__nome = nome

    def get_nome(self)-> str:
        return self.__nome

    def set_categoria(self)-> None:
        categoria = input('Digite a categoria do seu produto: ')
        op = input('Voce deseja adicionar uma subcategoria ao produto?, 1-sim, 2- não')
        if op.lower() == '1':
            sub = input("Digite a subcategoria que deseja adicionar")
            cat = [categoria, [sub]]
            self.__categoria.append(cat)
        if op.lower() == '2':
            self.__categoria.append([categoria])

    def set_cat(self) -> None:
        cat= categorias.Categorias().get_categoria()
        for i in cat:
            print(i[0],'-',i[1])
        categoria = int(input('Digite o valor da categoria do seu produto: '))
        for i in cat:
            if i[0]== categoria:
                self.__categoria.append(i)



    def get_categoria(self)-> list:
        return self.__categoria

    def set_descricao(self)-> None:
        while(True):
            descricao = input('Digite a descrição do seu produto OBS:(a descição deve ter mais de 20 caracteres): ')
            if len(descricao) >= 20:
                self.__descricao = descricao
                break

    def get_descricao(self)-> str:
        return self.__descricao

    def set_valor(self)-> None:
        while(True):
            try:
                valor = float(input("Digite o valor do produto: "))
                if valor>0:
                    self.__valor = valor
                    break
                elif valor <= 0:
                    print("o valor deve ser maior que 0")
            except ValueError as err:
                print('Você deve digitar o valor em numeros ex: 1200')

    def get_valor(self)-> float:
        return self.__valor

    def set_id(self,id:int)-> None:
        self.__id = id

    def get_id(self)->int:
        return self.__id

    def set_peso(self)-> None:
        while (True):
            try:
                peso = float(input("Digite o peso do produto em gramas: "))
                if peso > 0:
                    self.__peso = peso
                    break
                elif valor <= 0:
                    print("o peso deve ser maior que 0")
            except ValueError as err:
                print('Você deve digitar o peso em numeros ex: 100')

    def get_peso(self)->float:
        return self.__peso

    def set_largura(self)-> None:
        while (True):
            try:
                largura = float(input("Digite a largura do produto em centimetros: "))
                if largura > 0:
                    self.__largura = largura
                    break
                elif largura <= 0:
                    print("o peso deve ser maior que 0")
            except ValueError as err:
                print('Você deve digitar a largura em centimetros ex: 100')

    def get_largura(self)->float:
        return self.__largura

    def set_altura(self)-> None:
        while (True):
            try:
                altura = float(input("Digite a peso do altura em centimetros: "))
                if altura > 0:
                    self.__altura = altura
                    break
                elif altura <= 0:
                    print("a altura deve ser maior que 0")
            except ValueError as err:
                print('Você deve digitar a altura em centimetros ex: 100')

    def get_altura(self)->float:
        return self.__altura