CREATE DATABASE IF NOT EXISTS cadastro_cliente
DEFAULT CHARSET = utf8mb4
DEFAULT COLLATE = utf8mb4_general_ci;

USE cadastro_cliente;

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    email VARCHAR(100) UNIQUE NOT NULL
) DEFAULT CHARSET = utf8mb4;