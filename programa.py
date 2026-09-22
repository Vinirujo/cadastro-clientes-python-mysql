import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conexao.cursor()

while True:
    print("\n===== CADASTRO DE CLIENTES =====")
    print("1 - Cadastrar clientes")
    print("2 - Listar clientes")
    print("3 - Atualizar clientes")
    print("4 - Excluir clientes")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input ("Coloque o nome: ")
        data_nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
        email = input("Digite o email: ")
        
        sql = """
        insert into clientes (nome, data_nascimento, email) 
        values (%s, %s, %s)
        """
        
        dados = (nome, data_nascimento, email)
         
        cursor.execute(sql, dados)
        conexao.commit()
        
        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        
        if resultados:
            for cliente in resultados:
                print(cliente)
                
        else:
            print("Nenhum cliente encontrado.")        

    elif opcao == "3":
        id_cliente = int(input("Coloque o ID do cliente: "))
        novo_email = input("Digite o novo email: ")
                
        sql = """
            UPDATE clientes 
            set email = %s 
            WHERE id = %s
            """ 

                
        dados = (novo_email, id_cliente)
                
        cursor.execute(sql, dados)
        conexao.commit()
                
        if cursor.rowcount > 0:
            print("Cliente atualizado com sucesso!")
        else:
            print("Nenhum cliente encontrado com esse ID.")

    elif opcao == "4":
        id_cliente = int(input("Digite o id do cliente: "))
        
        confirmacao = input("Tem certeza que você quer excluir este cliente?(S/N): ").upper()
        
        if confirmacao == "S":
            sql = "DELETE FROM clientes WHERE id = %s"
            
            dados = (id_cliente,)
            
            cursor.execute(sql, dados)
            conexao.commit()
            
            if cursor.rowcount > 0:
                print("Cliente excluído com sucesso!")
            else:
                print("Nenhum cliente encontrado com esse ID.")

        else:
            print("Exclusão cancelada.")
            

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")