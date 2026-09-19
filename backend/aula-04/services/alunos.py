from database import create_conection

def find_all():
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("SELECT * FROM aluno")
                alunos = cursor.fetchall()

                return alunos

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao buscar os alunos{e}")
        raise

def find_by_id(aluno_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("SELECT * FROM aluno WHERE id = %s",(aluno_id,))
                aluno = cursor.fetchone()

                return aluno
     
    except Exception as e:
            print(f"[ERROR] ocorreu um erro ao buscar o aluno{e}")
            raise

def create_aluno(nome,curso,idade):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    INSERT INTO aluno(nome,curso,idade)
                    VALUES (%s, %s, %s)
                    """,
                    (nome,curso,idade)
                )
                connection.commit()

                id_aluno = cursor.lastrowid

                return id_aluno
            
    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao cadastrar o aluno{e}")
        raise

def update_aluno(nome, curso, idade, aluno_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("""
                    UPDATE aluno SET
                        nome = %s,
                        curso = %s,
                        idade = %s
                    WHERE id = %s
                """,(nome, curso, idade, aluno_id))

                connection.commit()
                if cursor.rowcount > 0:
                    return cursor.lastrowid

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao atualizar aluno{e}")
        raise

def delete_aluno(aluno_id):
    try:
        with create_conection() as connection:
            with connection.cursor(dictionary = True) as cursor:
                cursor.execute("DELETE FROM aluno WHERE id = %s",(aluno_id,))

                connection.commit()

    except Exception as e:
        print(f"[ERROR] ocorreu um erro ao deletar aluno{e}")
        raise