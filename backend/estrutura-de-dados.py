# lista

livros = ["Dom Casmurro","1984","O Hobbit"]
idades = [10, 40, 50]
nomes = ["Alice","Bob", "Charlie"]
dados = [1, "texto", 3.14, True]

#Adicionando elementos a lista
livros.append("O Senhor dos Aneis")

#Removendo Elementos da lista
livros.remove("1984")

#Inserindo elementos a lista no elemento 1
livros.insert(1, "O pequeno Principe")

# De i = 0 ate o tamanho da lista de livros, faça:
print("Inteirando sobre a lista de livros: ")
for i in range(len(livros)):
    print(livros[i])

# Maneira simplificada
for livro in livros:
    print(livro)

#dicionario

livro = {
    "id" : 1,
    "titulo" : "Dom Casmurro",
    "autor" : "machado de Assis"
}

# Lista de dicionarios

livros = [
    {
    "id" : 1,
    "titulo" : "Dom Casmurro",
    "autor" : "machado de Assis"
    },
     {
        "id" : 2,
        "titulo" : "1984",
        "autor" : "George Orwell"
    },
     {
        "id" : 3,
        "titulo" : "O Hobbit",
        "autor" : "J.R.R. Tolken"
    }
]