# 📊 Lista de Exercícios: Consultas SQL

Este documento contém uma seleção de exercícios de SQL divididos por nível de complexidade e comandos utilizados.

---

## 🟢 Básicas

> **1.** Liste todos os alunos.
```sql
SELECT * FROM aluno;
```

> **2.** Liste apenas nome e curso dos alunos.
```sql
SELECT nome, curso FROM aluno;
```


> **3.** Liste os livros ordenados por ano de publicação.
```sql
SELECT * FROM livro ORDER BY ano_publicacao ASC;
```


> **4.** Mostre os 2 livros mais recentes.
```sql
SELECT * FROM livro ORDER BY ano_publicacao DESC LIMIT 2;

```


> **5.** Liste categorias sem repetição.
```sql


```


---

## 🟡 Filtros (WHERE / BETWEEN / IN)

> **6.** Liste alunos com idade entre 20 e 23 anos.
```sql
SELECT * FROM aluno WHERE idade BETWEEN 20 AND 23;

```


> **7.** Liste livros publicados entre 2000 e 2020.
```sql
SELECT * FROM livro WHERE ano_publicacao BETWEEN 2000 AND 2020;

```


> **8.** Liste livros das categorias *Tecnologia* e *Ciência*.
```sql
SELECT * FROM livro WHERE fk_categoria_id IN (1,4);

```


---

## 🟠 Junções (JOIN)

> **9.** Liste o nome do aluno e o título do livro emprestado.
```sql
SELECT 
    a.nome,
    l.titulo
FROM emprestimo e
JOIN aluno a ON e.fK_aluno_id = a.id
JOIN livro l ON e.fk_livro_id = l.id;

```


> **10.** Liste o nome do aluno, livro e data do empréstimo.
```sql
SELECT 
    a.nome,
    l.titulo,
    e.data_emprestimo
FROM emprestimo e
JOIN aluno a ON e.fk_aluno_id = a.id
JOIN livro l ON e.fk_livro_id = l.id;

```


> **11.** Liste todos os livros e suas categorias.
```sql
SELECT 
    c.nome,
    l.titulo
FROM categoria c
JOIN livro l ON c.id = l.fk_categoria_id;

```


---

## 🔵 Agrupamento e Agregação (GROUP BY / FUNCTIONS)

> **12.** Conte quantos alunos existem.
```sql
SELECT COUNT(*) AS total_alunos
FROM aluno;
```


> **13.** Conte quantos empréstimos cada aluno realizou.
```sql
SELECT 
    a.nome,
COUNT(*) AS total_emprestimos
FROM emprestimo e
LEFT JOIN aluno a ON e.fK_aluno_id = a.id
GROUP BY a.nome
;


```


> **14.** Mostre a média de idade dos alunos.
```sql
SELECT AVG(idade) AS media_idade
 FROM aluno;
```


> **15.** Mostre a quantidade de livros por categoria.
```sql
SELECT 
    c.nome,
COUNT(*) AS qntd_livros
FROM livro l
LEFT JOIN categoria c ON l.fK_categoria_id = c.id
GROUP BY c.nome
;

```


> **16.** Mostre o livro mais antigo.
```sql 
SELECT titulo, ano_publicacao
 FROM livro ORDER BY ano_publicacao LIMIT 1;

```


> **17.** Mostre o livro mais recente.
```sql
SELECT titulo, ano_publicacao
 FROM livro ORDER BY ano_publicacao DESC LIMIT 1;

```


---

## 🔴 Subconsultas (SUBQUERY)

> **18.** Liste os livros publicados acima da média de ano de publicação.
```sql
SELECT titulo, ano_publicacao FROM livro
WHERE ano_publicacao < (SELECT AVG(ano_publicacao) 
FROM livro);


```


> **19.** Mostre o aluno que realizou mais empréstimos.
```sql
SELECT nome 
FROM aluno WHERE id = (
SELECT fk_aluno_id 
FROM emprestimo
GROUP BY fk_aluno_id
ORDER BY COUNT(*) DESC LIMIT 1
);


```


> **20.** Liste livros que nunca foram emprestados.
```sql
SELECT * FROM livro
WHERE id  IN (
SELECT fk_livro_id FROM emprestimo 
);

```
