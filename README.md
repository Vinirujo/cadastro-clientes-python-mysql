# Cadastro de Clientes com Python e MySQL

Projeto de estudo desenvolvido para praticar a integração entre
Python e MySQL.

## Funcionalidades

- Cadastro de clientes
- Consulta de clientes

## Tecnologias utilizadas

- Python
- MySQL
- MySQL Connector/Python
- Python Dotenv
- Git e GitHub

## Como executar o projeto

### 1. Instale as dependências

No terminal, execute:

```bash
python -m pip install mysql-connector-python python-dotenv
```

### 2. Prepare o banco de dados

Abra o arquivo `banco.sql` no MySQL Workbench e execute seus comandos para criar o banco e a tabela.

### 3. Configure a conexão

Crie um arquivo chamado `.env` na pasta do projeto, seguindo o modelo disponível em `.env.example`.

Preencha as informações de conexão com o seu MySQL.

**Não publique o arquivo `.env`, pois ele contém sua senha.**

### 4. Execute o programa

No terminal, execute:

```bash
python programa.py
```

O programa solicitará o nome, a data de nascimento e o e-mail do cliente. Após o cadastro, mostrará os clientes registrados.