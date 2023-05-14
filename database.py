def create_table(c):
    c.execute("""
    CREATE TABLE servidores (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            sigla TEXT NOT NULL
    );
    """)
    print('Tabela criada com sucesso.')

def insert_table(c, data):
    c.execute("INSERT INTO servidores (url, sigla) VALUES (?,?)", (data['url'], data['sigla']))
    print('Dados inseridos com sucesso')
