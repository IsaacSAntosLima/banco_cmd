INSERT INTO categoria(nome) VALUES
('Tecnologia'),
('Romance'),
('História'),
('Ciência');

INSERT INTO aluno(nome, curso, idade) VALUES
('João', 'Sistemas de Informação', 22),
('Maria', 'Direito', 25),
('Carlos', 'Engenharia', 21),
('Ana', 'Medicina', 24);

INSERT INTO livro(titulo, autor, ano_publicacao, fk_categoria_id) VALUES
('Clean Code', 'Robert Martin', 2008, 1),
('Dom Casmurro', 'Machado de Assis', 1899, 2),
('Sapiens', 'Yuval Harari', 2011, 3),
('Cosmos', 'Carl Sagan', 1980, 4);

INSERT INTO emprestimo(data_emprestimo, data_devolucao, fk_aluno_id, fk_livro_id) VALUES
('2026-05-01', '2026-05-10', 1, 1),
('2026-05-03', '2026-05-12', 2, 2),
('2026-05-05', '2026-05-15', 1, 3),
('2026-05-07', '2026-05-17', 3, 1);