import product

class menu:
    listProdutos = []
    produto= product.Produto()

    def Inserir(self):
        novo_produto = []
        self.produto.id=len(self.listProdutos)
        print("Escreva os valores para o seu novo produto")
        print("NOME | DESCRICAO | VALOR | CATEGORIA")
        self.produto.set_nome()
        self.produto.set_descricao()
        self.produto.set_valor()
        #self.produto.set_categoria()
        self.produto.set_cat()
        self.produto.set_peso()
        self.produto.set_altura()
        self.produto.set_largura()
        self.listProdutos.append(self.produto)

    def Alterar(self):
        referencia = input("Para alterar um produto basta digitar o nome dele")
        for i in range(len(self.listProdutos)):
            if self.listProdutos[i].get_nome() == referencia:
                print("vai dar erro")
                print("Escreva os valores para alterar o seu produto")
                print("NOME | DESCRICAO | VALOR | CATEGORIA")
                self.listProdutos[i].set_nome()
                self.listProdutos[i].set_descricao()
                self.listProdutos[i].set_valor()
                #self.listProdutos[i].set_categoria()
                self.listProdutos[i].set_cat()
                self.listProdutos[i].set_peso()
                self.listProdutos[i].set_altura()
                self.listProdutos[i].set_largura()
            else:
                print("Não foi encontrado o produto")

    def Deletar(self):
        referencia = input("Para deletar um produto basta digitar o nome dele")
        for i in range(len(self.produto)):
            if self.listProdutos[i].get_nome() == referencia:
                del(self.listProdutos[i])
                print("deletado com sucesso")

    def Selecionar(self):
        opcao=input("Selecione um numero de acordo com sua opção de filtro: 1- Nome, 2- Descrição, 3- Valor, 4- Categoria, 5- listar todos seus produtos")

        if opcao == '1':
            filtro = input("Digite o nome que deseja filtrar")
            for i in range(len(self.listProdutos)):
                if self.listProdutos[i].get_nome() == filtro.lower():
                    print("Nome:", self.listProdutos[i].get_nome()," Descrição:",self.listProdutos[i].get_descricao(),
                          " Valor:",self.listProdutos[i].get_valor()," Categoria:",
                          self.listProdutos[i].get_categoria()[i][1])

        if opcao == '2':
            filtro = input("Digite a Descrição que deseja filtrar")
            for i in range(len(self.listProdutos)):
                if filtro.lower() in self.listProdutos[i].get_descricao().lower():
                    print("Nome:", self.listProdutos[i].get_nome(), " Descrição:", self.listProdutos[i].get_descricao(),
                          " Valor:", self.listProdutos[i].get_valor(), " Categoria:",
                          self.listProdutos[i].get_categoria()[i][1])
        if opcao == '3':
            filtro = int(input("Digite o valor que deseja filtrar"))
            for i in range(len(self.listProdutos)):
                if filtro > self.listProdutos[i].get_valor():
                    print("Nome:", self.listProdutos[i].get_nome(), " Descrição:", self.listProdutos[i].get_descricao(),
                          " Valor:", self.listProdutos[i].get_valor(), " Categoria:",
                          self.listProdutos[i].get_categoria()[i][1])
        if opcao == '4':
            filtro = input("Digite a Categoria que deseja filtrar")
            for i in range(len(self.listProdutos)):
                if filtro.lower() in self.listProdutos[i].get_categoria()[i]:
                    print("Nome:", self.listProdutos[i].get_nome(), " Descrição:", self.listProdutos[i].get_descricao(),
                          " Valor:", self.listProdutos[i].get_valor(), " Categoria:",
                          self.listProdutos[i].get_categoria()[i][1])
        if opcao == '5':
            for i in range(len(self.listProdutos)):
                print("Nome:", self.listProdutos[i].get_nome(), " Descrição:", self.listProdutos[i].get_descricao(),
                      " Valor:", self.listProdutos[i].get_valor(), " Categoria:",
                      self.listProdutos[i].get_categoria()[i][1])







user=menu()
print("Seja bem vindo ao sistema de gestão de produtos")
while(True):
    print("Digite o valor para realizar a ação")
    op=input("1- Cadastrar novo produto, 2- Alterar um produto, 3- Deletar um produto, 4- Selecionar Produtos")
    if op == '1':
        user.Inserir()
    if op == '2':
        user.Alterar()
    if op == '3':
        user.Deletar()
    if op == '4':
        user.Selecionar()
    else:
        print("Selecione o numero de acordo com a opção")
