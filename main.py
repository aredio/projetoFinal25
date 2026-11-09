#O código do seu programa vai ser desenvolvido aqui. Siga o README.md cuidadosamente!
listaDeProdutos = []
opcao = -1
while(opcao != 0):
    print("Sistema de Estoque")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")
    opcao = int(input("Digite a opção desejada:"))
    if(opcao == 1):
        print("Você escolheu: Cadastrar produto")
        codigo = int(input("Digite o código do produto:"))
        nome = input("Digite o nome do produto:")
        preco = float(input("Digite o preço do produto:R$"))
        categoria = input("Digite a categoria do produto:")
        quantidade = int(input("Quantidade em estoque do produto: "))
        produto = [codigo,nome,preco,categoria,quantidade]
        listaDeProdutos.append(produto)
    elif(opcao == 2):
        print("Você escolheu: Listar produtos")
        for produto in listaDeProdutos:
            print("Código do produto: ",produto[0])
            print("Nome do produto: ", produto[1])
            print("Preço do produto: ", produto[2])
            print("Categoria do produto: ", produto[3])
            print("Quantidade em estoque: ", produto[4])
            print("=============")
    elif(opcao == 0):
        print("Você escolheu Sair do programa")
        break
    else:
        print("Opção inválida")
