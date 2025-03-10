import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'costumers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#SQL
#Criando a tabela

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

#CUIDADO: fazendo delete sem where - Apaga os dados mas n reseta a contagem do ID
cursor.execute(f'DELETE FROM {TABLE_NAME}')

#Apaga os dados e zera a contagem do ID
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')

#Registrar valores na coluna da tabela
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight)'
    'VALUES (NULL, "Léo", 90)'
)
connection.commit()

cursor.close()
connection.close()