from datetime import date

from database import create_conection

def find_all():
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    SELECT 
                        e.id,
                        e.data_emprestimo,
                        e.data_devolucao,
                        e.fk_aluno_id,
                        e.fk_livro_id
                    FROM emprestimo e
                    ORDER BY e.id
                """)

                return cursor.fetchall()
            
    except Exception as e:
            print(f"[ERROR] ocorreu um erro ao buscar os emprestimos{e}")
            raise

def find_by_id(emprestimo_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                     SELECT 
                        e.id,
                        e.data_emprestimo,
                        e.data_devolucao,
                        e.fk_aluno_id,
                        e.fk_livro_id
                    FROM emprestimo e
                    WHERE e.id = %s
                """, (emprestimo_id,))

                return cursor.fetchone()

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao buscar o emprestimo{e}")
        raise

def aluno_existe(aluno_id):

    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    SELECT id
                    FROM aluno
                    WHERE id = %s
                """,(aluno_id,))

                return cursor.fetchone() is not None

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao verificar o aluno{e}")
        raise

def livro_existe(livro_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    SELECT id
                    FROM livro
                    WHERE id = %s
                """,(livro_id,))

                return cursor.fetchone() is not None

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao verificar o livro{e}")
        raise

def livro_disponivel(livro_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    SELECT id 
                    FROM emprestimo
                    WHERE fk_livro_id = %s
                    AND data_devolucao IS NULL 
                """,(livro_id,))

                return cursor.fechone() is None

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao verificar disponibilidade{e}")
        raise

def create_emprestimo(aluno_id, livro_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    INSERT INTO emprestimo (
                        data_emprestimo,
                        data_devolucao,
                        fk_aluno_id,
                        fk_livro_id
                    )
                    VALUES (%s,%s,%s,%s)
                """, (
                        date.today(),
                        None,
                        aluno_id,
                        livro_id
                ) )

                connection.commit()

                emprestimo_id = cursor.lastrowid

                return find_by_id(emprestimo_id)

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao criar emprestimo{e}")
        raise

def devolver_livro(emprestimo_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    UPDATE emprestimo 
                    SET data_devolucao = %s
                    WHERE id = %s
                """,(
                        date.today(),
                        emprestimo_id      
                ))
                connection.commit()

                return find_by_id(emprestimo_id)

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao registrar a devolucao{e}")
        raise

def delete_emprestimo(emprestimo_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    DELETE FROM emprestimo
                    WHERE id = %s
                """,(emprestimo_id,))
                connection.commit()

                return cursor.rowcount > 0

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao excluir emprestimo{e}")
        raise

def find_abertos():
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    SELECT 
                        e.id,
                        a.nome AS aluno,
                        l.titulo AS livro,
                        e.data_emprestimo
                    FROM emprestimo e
                    INNER JOIN aluno a
                        ON a.id = e.fk_aluno_id
                    INNER JOIN livro l
                        ON l.id = e.fk_livro_id
                    WHERE e.data_devolucao IS NULL
                    ORDER BY e.data_emprestimo
                """)
                return cursor.fetchall()
    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao buscar pelos livros abertos{e}")
        raise