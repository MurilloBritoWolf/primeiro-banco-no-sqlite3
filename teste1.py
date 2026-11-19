import sqlite3

try:
    banco = sqlite3.connect('banco.db')

    cursor = banco.cursor()

    cursor.execute("CREATE TABLE aluno(id_aluno int, Nome text, idade int, email text)")

    cursor.execute("INSERT INTO aluno VALUES (1, 'JOÃO',20,'joaozinholeroy@gmail.com') ")
    cursor.execute("INSERT INTO aluno VALUES (2, 'jheimes',25,'rick@gmail.com') ")
    cursor.execute("INSERT INTO aluno VALUES (3, 'ricardo',26,'jheimesbrow@gmail.com') ")
    banco.commit()
    print("Os dados foram adicionados com sucesso!!")


    cursor.execute("Select *FROM aluno")
    print(cursor.fetchall())

    cursor.execute("DELETE from aluno WHERE idade = 20")

    banco.commit()
    
    cursor.execute("""
    DELETE FROM aluno 
    WHERE rowid NOT IN (
        SELECT MIN(rowid)
        FROM aluno
        GROUP BY email
    )
""")
    banco.commit()
    banco.close()
    print("Os dados foram removidos com sucesso!!")

except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)
