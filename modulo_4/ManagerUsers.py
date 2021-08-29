from modulo_4.funcoes import *


usuarios = dict()
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    opcao = input("O que deseja realizar?" +
                  "\n<I> - Para Inserir um usuário" +
                  "\n<P> - Para Pesquisar um usuário" +
                  "\n<E> - Para Excluir um usuário" +
                  "\n<L> - Para Listar um usuário: ").upper()
    if opcao == "P":
        login = input('Qual login deseja buscar?: ').upper()
        pesquisar(usuarios, login)
    if opcao == "E":
        login = input('Qual login deseja apagar?: ').upper()
        excluir(usuarios, login)
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()
