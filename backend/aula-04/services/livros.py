from database import create_conection

def find_all():
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("SELECT * FROM livro")
                livros = cursor.fetchall()

                return livros


    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao buscar os livros{e}")
        raise

def find_by_id(livro_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("SELECT * FROM livro WHERE id = %s",(livro_id,))
                livro = cursor.fetchone()

                return livro
     
    except Exception as e:
            print(f"[ERROR] ocorreu um erro ao buscar os livros{e}")
            raise


def create_livro(titulo, autor, ano_publicacao, fk_categoria_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    INSERT INTO livro(titulo, autor, ano_publicacao, fk_categoria_id) 
                    VALUES (%s, %s, %s, %s)
                    """,
                    (titulo, autor, ano_publicacao, fk_categoria_id)
                )
                connection.commit()

                id_livro = cursor.lastrowid

                return id_livro
            
    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao cadastrar o livro{e}")
        raise


def update_livro(titulo, autor, ano_publicacao, fk_categoria_id, livro_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    UPDATE livro SET
                        titulo = %s,
                        autor = %s,
                        ano_publicacao = %s,
                        fk_categoria_id = %s
                    WHERE id = %s
                """,(titulo,autor,ano_publicacao,fk_categoria_id,livro_id))

                connection.commit()
                if cursor.rowcount > 0:
                    return cursor.lastrowid

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao cadastrar o livro{e}")
        raise

def delete_livro(livro_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("DELETE FROM livro WHERE id = %s",(livro_id,))

                connection.commit()

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao cadastrar o livro{e}")
        raise