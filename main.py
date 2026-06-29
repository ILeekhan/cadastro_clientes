# Importa a ferramenta para trabalhar com o banco SQLite
import sqlite3

# Função para conectar ao banco
def conectar():
    return sqlite3.connect("database/cadastro.db")

# Função para criar a tabela
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE,
        telefone TEXT,
        cidade TEXT
    )
    """)
    conn.commit()
    conn.close()

# Cadastrar
def cadastrar(nome, email, telefone, cidade):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone, cidade)
            VALUES (?, ?, ?, ?)
        """, (nome, email, telefone, cidade))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Listar todos
def listar_todos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

# Buscar por nome
def buscar_por_nome(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE ?", (f"%{nome}%",))
    return cursor.fetchall()

# Atualizar
def atualizar(id, nome, email, telefone, cidade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE clientes SET nome=?, email=?, telefone=?, cidade=?
        WHERE id=?
    """, (nome, email, telefone, cidade, id))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

# Excluir
def excluir(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

# Menu
def menu():
    criar_tabela()
    while True:
        print("\n===== SISTEMA DE CADASTRO =====")
        print("1 - Cadastrar")
        print("2 - Listar todos")
        print("3 - Buscar por nome")
        print("4 - Atualizar")
        print("5 - Excluir")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            cidade = input("Cidade: ")
            if cadastrar(nome, email, telefone, cidade):
                print("✅ Cadastrado!")
            else:
                print("❌ E-mail já existe!")

        elif opcao == "2":
            for c in listar_todos():
                print(f"ID: {c[0]} | Nome: {c[1]} | E-mail: {c[2]} | Cidade: {c[4]}")

        elif opcao == "3":
            termo = input("Nome: ")
            for c in buscar_por_nome(termo):
                print(f"ID: {c[0]} | {c[1]} | {c[3]}")

        elif opcao == "4":
            try:
                id = int(input("ID: "))
                nome = input("Novo nome: ")
                email = input("Novo e-mail: ")
                telefone = input("Telefone: ")
                cidade = input("Cidade: ")
                if atualizar(id, nome, email, telefone, cidade):
                    print("✅ Atualizado!")
                else:
                    print("❌ ID não encontrado")
            except:
                print("❌ Digite um número válido")

        elif opcao == "5":
            try:
                id = int(input("ID: "))
                if excluir(id):
                    print("✅ Excluído!")
                else:
                    print("❌ ID não encontrado")
            except:
                print("❌ Digite um número válido")

        elif opcao == "6":
            print("👋 Saindo...")
            break

        else:
            print("⚠️ Opção inválida")

if __name__ == "__main__":
    menu()