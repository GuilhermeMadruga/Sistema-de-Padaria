CREATE DATABASE padaria;

\c padaria;

-- Criando a tabela de produtos com a coluna 'ativo'
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    ativo BOOLEAN DEFAULT TRUE -- Indica se o produto está ativo ou inativo
);

-- Criando a tabela de pedidos com todas as colunas atualizadas
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nome_produto VARCHAR(255), -- Armazena o nome do produto no momento do pedido
    preco_unitario DECIMAL(10, 2), -- Armazena o preço unitário do produto no momento do pedido
    cancelado BOOLEAN DEFAULT FALSE, -- Indica se o pedido foi cancelado
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);