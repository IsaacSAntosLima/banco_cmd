import mysql.connector                  
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_HOST = os.getenv("HOST")
SERVER_USER = os.getenv("USER")
SERVER_PASSWORD = os.getenv("PASSWORD")
SERVER_DATABASE = os.getenv("DATABASE")

def create_conection():
    try:
        conexao = mysql.connector.connect(
            host=SERVER_HOST,
            user=SERVER_USER,
            password=SERVER_PASSWORD,
            database=SERVER_DATABASE,
        )

        if conexao.is_connected():
            print(f"[INFO] conexão com banco de dados estabelecida")
        return conexao

    except mysql.connector.Error as e:
        print(f"[ERROR] ocorreu um erro ao conectar ao mysql {e}")
        raise

