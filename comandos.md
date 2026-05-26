# Comandos SQL
#### mostra os bancos de dados instalados no servidor
``` sql
 SHOW DATABASES;
 ```
#### conectar a um dos bancos 
``` sql
USE (nome do banco);
```
#### Mostra as tabelas do banco selecionado

``` sql
SHOW TABLES; 
```
#### Cria um banco de dados
``` sql
CREATE DATABASE (nome do banco);
```
#### Traz os dados da tabela
``` sql
SELECT * FROM (nome da tabela);
```
#### Insere valores na tabela
``` sql
INSERT INTO nome_da_tabela(nome_do_campo) VALUES (nome_valores);
```
#### Selecionar uma tupla especifica
``` sql
SELECT * FROM nome_da_tabela WHERE nome_do_campo = valor;
```
#### Seleciona os dados da tabela trazendo so um campo especifico
``` sql
SELECT nome_do_campo FROM nome_da_tabela ;
```
#### Atualiza os dados de um campo especifico
``` sql
UPDATE nome_da_tabela SET nome_do_campo = valor_do_campo WHERE nome_do_campo = valor_do_campo;
```
#### Apaga os dados de uma tupla
``` sql
DELETE FROM nome_da_tabela WHERE nome_do_campo = valor_do_campo;
```

#### Descreve a estrutura da tabela
``` sql
DESCRIBE nome_da_tabela ;
```

#### Ordena e limita uma ordem especifica (DESC, ASC)
``` sql
SELECT *
FROM    nome_da_tabela
ORDER BY nome_do_campo DESC
LIMIT valor;
```

#### Traz os valores sem repetições
``` sql
SELECT DISTINCT nome_do_campo
FROM nome_da_tabela ;
```

#### Traz valores entre um e outro
``` sql
SELECT *
FROM nome_da_tabela
WHERE nome_do_campo BETWEEN valor_1 AND valor_2;
```

#### Traz valores especificos (String, Num)
``` sql
SELECT *
FROM nome_da_tabela
WHERE nome_do_campo IN ('valor_do_campo', 'valor_do_campo');
```

### usando operadores { =, <, >, >=, <=, <>, != }
``` sql
SELECT *
FROM nome_da_tabela
WHERE valor_do_campo operadores valor;

```

### usando filtro de semelhança
``` sql
SELECT *
FROM nome_da_tabela
WHERE valor_do_campo LIKE valor;

```

### Usando JOIN
Junta os valores de duas tabelas
``` sql
SELECT 
    nome_do_campo_da_tabela_1,
    nome_do_campo_da_tabela_2
FROM    tabela_1
JOIN tabela_2 ON tabela_1.valor_do_id = tabela_2.valor_do_fk;
```
***
## Classificação (DDL, DML e DQL)

* DDL: Os comandos DDL são usados para definir, alterar ou remover a estrutura dos objetos do banco de dados
* DML: Manipula e gerencia os dados das tabelas
* DQL: É utilizado para consultar as tabelas

## Resumo das classificações

| Sigla | Nome | Função |
|---|---|---|
| DDL | Data Definition Language | Define estruturas do banco (CREATE, ALTER, DROP) |
| DQL | Data Query Language | Consulta dados (`SELECT`, `SHOW`, `DESCRIBE`) |
| DML | Data Manipulation Language | Manipula dados (`INSERT`, `UPDATE`, `DELETE`) |