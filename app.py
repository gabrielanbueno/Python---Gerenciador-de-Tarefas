import sqlite3

def create_connection():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        status TEXT DEFAULT 'Pendente')""")
    conn.commit()
    return conn, cursor

def add_tarefa():
    titulo = input("Digite o título da tarefa: ").strip()
    if not titulo:
        print("O título da tarefa não pode estar vazio.")
        return
    
    conn, cursor = create_connection()
    cursor.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
    conn.commit()
    conn.close()
    print("Tarefa adicionada com sucesso.")
    
def listar_tarefas():
    conn, cursor = create_connection()    
    cursor.execute("SELECT id, titulo, status FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    print("LISTA DE TAREFAS:")
    for id_tarefa, titulo, status in tarefas:
        print(f"ID: [{id_tarefa}] Título: {titulo} - Status: {status}")
    print("-" * 50)
    
def concluir_tarefa():
    listar_tarefas()
    try:
        id_tarefa = int(input("Digite o ID da tarefa que deseja concluir: "))
    except ValueError:
        print("ID inválido. Por favor, insira um número inteiro.")
        return
    conn, cursor = create_connection()
    cursor.execute(
        "UPDATE tarefas SET status = 'Concluída' WHERE id = ?", (id_tarefa,)
    )
    
    if cursor.rowcount > 0:
        conn.commit()
        print("Tarefa atualizada, para serr concluída.")
    else:
        print("Tarefa não encontrada.")
    conn.close()
    
def deletar_tarefa():
    listar_tarefas()
    try:
        id_tarefa = int(input("Digite o ID da tarefa que deseja deletar: "))
    except ValueError:
        print("ID inválido. Por favor, insira um número inteiro.")
        return
    
    conn, cursor = create_connection()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    
    if cursor.rowcount > 0:
        conn.commit()
        print("Tarefa deletada com sucesso.")
    else:
        print("Tarefa não encontrada.")
    conn.close()
    
def main():
    while True:
        print("\nMENU DE TAREFAS")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Deletar tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            add_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            concluir_tarefa()
        elif opcao == '4':
            deletar_tarefa()
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
                    
if __name__ == "__main__":
    main()
    
    
