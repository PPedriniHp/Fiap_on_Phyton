with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tao facil criar um arquivo.")


with open("teste.txt", "a") as arquivo:
    arquivo.write("Teste do A no open, para ver se o append funciona.")