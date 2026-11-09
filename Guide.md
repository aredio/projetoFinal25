# Projeto Final: Sistema de Controle de Estoque em Python

## 1. Funcionalidades do Sistema Final

O sistema deverá possuir um menu principal com a seguinte estrutura de opções:

```text
================================
       SISTEMA DE ESTOQUE
================================

1 - Cadastrar produto
2 - Listar produtos
3 - Consultar produto
4 - Registrar entrada
5 - Registrar saída
6 - Excluir produto
7 - Relatório de estoque
0 - Sair

Escolha uma opção:
```

### Atributos do Produto
Cada produto cadastrado deverá conter:
- **Código identificador**
- **Nome**
- **Categoria**
- **Preço**
- **Quantidade em estoque**

---

## 2. Estrutura Inicial e Cadastro de Produtos

**Objetivo:** Construir a primeira versão do sistema utilizando variáveis, listas, condicionais e laços de repetição.  
*Cenário:* Uma loja precisa de um programa para controlar seus produtos, pois atualmente realiza esse controle manualmente.

### Criando a Estrutura Básica
Inicialize a lista que armazenará os dados e a variável de controle da navegação:

```python
produtos = []
opcao = -1
```

### Construindo o Menu Principal
Implementação do laço de repetição `while` com a estrutura condicional `if/elif/else`:

```python
while opcao != 0:
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        print("Cadastrar produto")
    elif opcao == 2:
        print("Listar produtos")
    elif opcao == 0:
        print("Encerrando sistema")
    else:
        print("Opção inválida")
```

---

## 3. Implementando o Cadastro

Nesta etapa, cada produto é representado por uma lista contendo seus dados em posições fixas:

```python
codigo = input("Código: ")
nome = input("Nome: ")
categoria = input("Categoria: ")
preco = float(input("Preço: "))
quantidade = int(input("Quantidade: "))

produto = [codigo, nome, categoria, preco, quantidade]
produtos.append(produto)
```

---

## 4. Listagem de Produtos

Utilize a estrutura de repetição `for` para iterar sobre a lista principal e exibir as informações de cada item:

```python
for produto in produtos:
    print("Código:", produto[0])
    print("Nome:", produto[1])
    print("Categoria:", produto[2])
    print("Preço:", produto[3])
    print("Estoque:", produto[4])
    print("-" * 20)
```

---

## 5. Consultas e Movimentação de Estoque

Permite localizar um produto por meio do seu código identificador para exibir dados ou atualizar quantidades.

### Conceitos Utilizados
- Percorrer listas com `for`
- Comparar valores com `if`
- Utilizar variáveis de controle (flags)

### Entrada de Produtos
Registra a chegada de novas unidades ao estoque atual.  
*Exemplo:* Um produto com 10 unidades recebe mais 5, totalizando 15 unidades.

```python
codigo = input("Código do produto: ")

for produto in produtos:
    if produto[0] == codigo:
        quantidade = int(input("Quantidade recebida: "))
        produto[4] += quantidade
        print("Entrada registrada!")
```

### Saída de Produtos
Registra a saída/venda de mercadorias, validando previamente se há saldo suficiente disponível:

```python
codigo = input("Código do produto: ")

for produto in produtos:
    if produto[0] == codigo:
        quantidade = int(input("Quantidade retirada: "))
        if quantidade <= produto[4]:
            produto[4] -= quantidade
            print("Saída registrada!")
        else:
            print("Estoque insuficiente!")
```

---

## 6. Exclusão de Produtos

Permite remover permanentemente um registro de mercadoria da lista com base no código informado.
