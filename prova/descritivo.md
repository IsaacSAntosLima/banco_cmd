# Atividade Prática — Consultas SQL

## Objetivo
Aplicar os conhecimentos sobre consultas SQL usando um banco de dados de biblioteca.

## Descrição
O participante deverá importar o banco de dados disponibilizado e executar as consultas solicitadas, utilizando os comandos SQL estudados em aula. Durante as próximas duas semanas é permitido estudar e testar consultas; na apresentação final o banco será recriado e as consultas serão executadas ao vivo, com explicação da lógica.

## Instruções
- Importe o arquivo de dados fornecido (veja a pasta `mysql-init`).
- Crie e teste as consultas em um arquivo `consultas.sql` ou em um cliente MySQL.
- Prepare-se para executar as consultas ao vivo e explicar cada passo.

## Cronograma
- Período de estudo e prática: 2 semanas

## Conteúdos esperados
- `SELECT`
- `WHERE`
- `ORDER BY`
- `DISTINCT`
- `IN`
- `BETWEEN`
- `JOIN` (LEFT/RIGHT)
- `GROUP BY`
- `COUNT`, `AVG`, `SUM`
- Subqueries

## Exemplo de consultas
```sql
-- Selecionar títulos distintos
SELECT DISTINCT titulo
FROM livros;

-- Livros publicados entre 2000 e 2010
SELECT titulo, ano
FROM livros
WHERE ano BETWEEN 2000 AND 2010
ORDER BY ano DESC;

-- Total de livros por autor
SELECT a.nome, COUNT(l.id) AS total_livros
FROM autores a
JOIN livros l ON l.autor_id = a.id
GROUP BY a.nome
ORDER BY total_livros DESC;
```
