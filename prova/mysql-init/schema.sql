CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE aluno (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    curso VARCHAR(100),
    idade INT
);

CREATE TABLE categoria (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE livro (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100),
    ano_publicacao INT,
    fk_categoria_id BIGINT,
    
    FOREIGN KEY (fk_categoria_id)
    REFERENCES categoria(id)
);

CREATE TABLE emprestimo (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    data_emprestimo DATE,
    data_devolucao DATE,
    
    fk_aluno_id BIGINT,
    fk_livro_id BIGINT,
    
    FOREIGN KEY (fk_aluno_id)
    REFERENCES aluno(id),

    FOREIGN KEY (fk_livro_id)
    REFERENCES livro(id)
);