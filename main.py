from database.conexao import conectar

def cadastrarLivros():
    conexao = conectar()
    cursor = conexao.cursor()

    titulo = input('Digite o título do livro: ')
    autor = input('Digite o autor do livro: ')
    genero = input('Digite o genero do livro: ')
    editora = input('Digite o nome da editora: ')
    ano_publicado = input('Digite o ano publicado: ')

    sql = """INSERT INTO Livros (TITULO, AUTOR, GENERO, EDITORA, ANO_PUBLICADO) VALUES (%s, %s, %s, %s, %s);"""

    valores = (titulo, autor, genero, editora, ano_publicado)
    cursor.execute(sql, valores)