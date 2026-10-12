# Atividade — Regras de Negócio no Backend

**Tema:** Regras de negócio, responsabilidades do backend e integridade do banco de dados.

**Contexto:** Durante o desenvolvimento da API da biblioteca, foram implementadas funcionalidades para cadastrar alunos, livros e empréstimos. Diferentemente de um CRUD simples, o módulo de empréstimos precisa respeitar condições específicas, como verificar se o aluno existe, se o livro está disponível e se ele já foi devolvido.

O objetivo desta atividade é compreender o que são regras de negócio, por que são importantes e como se relacionam com o frontend e o banco de dados.

## Parte 1 — Compreendendo os conceitos

**1. O que são regras de negócio?**

Explique, com suas próprias palavras, o que são regras de negócio e apresente dois exemplos relacionados ao sistema da biblioteca.

**2. Qual é a importância das regras de negócio?**

Imagine um sistema que permite cadastrar empréstimos sem verificar se o livro já está emprestado. Quais problemas poderiam acontecer? Explique como as regras de negócio ajudam a evitar essas situações.

**3. Por que não deixar as regras de negócio somente no frontend?**

Imagine que o frontend bloqueia o botão de empréstimo quando um livro está indisponível.

- Por que essa validação, sozinha, não é suficiente?
- O que aconteceria se alguém fizesse uma requisição diretamente pelo Postman?
- Qual deve ser a responsabilidade do backend nessa situação?

**4. Qual é a responsabilidade do backend?**

Explique por que o backend precisa validar os dados recebidos e verificar as condições necessárias antes de executar uma operação no banco de dados.

**5. O que acontece quando uma regra de negócio é violada?**

Quando um aluno tenta emprestar um livro que já está emprestado, o sistema deve simplesmente executar a operação e registrar o problema depois? Justifique sua resposta e explique como a API deve comunicar a situação ao cliente.

## Parte 2 — Backend versus banco de dados

**6. Qual é a diferença entre regras de negócio e restrições do banco de dados?**

Explique a diferença entre as responsabilidades do backend e as do banco de dados. Considere que ambos podem contribuir para impedir operações inválidas.

**7. Analise os exemplos a seguir e identifique a principal responsabilidade de cada um:**

a) O backend verifica se um aluno está cadastrado antes de realizar um empréstimo.

b) O banco de dados impede que duas linhas possuam o mesmo valor de chave primária.

c) O backend verifica se um livro já possui um empréstimo em aberto.

d) O banco de dados impede que um empréstimo referencie um aluno que não existe, por meio de uma chave estrangeira.

e) O backend verifica se o empréstimo já foi devolvido antes de aceitar uma nova solicitação de devolução.

Para cada item, explique sua escolha.

**8. Por que não devemos depender exclusivamente do backend ou exclusivamente do banco de dados para garantir a validade das operações?**

Explique como a aplicação das validações no backend e das restrições adequadas no banco de dados pode contribuir para um sistema mais confiável.

## Parte 3 — Aplicando os conceitos à biblioteca

**9. Analise a seguinte situação:**

Dois usuários tentam emprestar o mesmo livro quase simultaneamente. Os dois pedidos verificam que o livro está disponível antes que qualquer um deles registre o empréstimo.

- Qual problema pode acontecer?
- Por que uma simples verificação no backend pode não ser suficiente?
- Que medidas poderiam ajudar a impedir que o livro fosse emprestado duas vezes?

**10. Imagine que a biblioteca decida implementar uma nova regra: cada aluno pode ter, no máximo, três empréstimos em aberto.**

Responda:

a) Qual seria a regra de negócio?

b) Em qual camada essa regra deveria ser implementada e por quê?

c) Que consulta ao banco de dados poderia ajudar a verificar quantos empréstimos em aberto o aluno possui?

d) O que a API deveria fazer quando o aluno já tivesse atingido o limite?

**11. Um desenvolvedor implementou a seguinte lógica:**

- O frontend verifica se o livro está disponível.
- O backend recebe a requisição e cadastra o empréstimo sem realizar nenhuma validação.
- O banco de dados possui chaves estrangeiras, mas não verifica se o livro já está emprestado.

Quais são os problemas dessa implementação? Proponha melhorias, indicando a responsabilidade de cada camada.

**12. Diferencie validação de dados e regra de negócio, utilizando exemplos da API da biblioteca.**

Considere situações como receber um identificador inválido, não informar um campo obrigatório ou tentar emprestar um livro que já está emprestado.

## Parte 4 — Reflexão final

**13. Explique o que significa dizer que o backend é responsável por aplicar as regras de negócio da aplicação.**

Sua resposta deve relacionar o frontend, o backend e o banco de dados.

**14. Em sua opinião, qual seria a consequência de implementar uma API que realiza todas as operações de CRUD corretamente, mas não possui regras de negócio?**

Utilize um exemplo concreto para justificar sua resposta.

## Orientações

- Responda com suas próprias palavras.
- Utilize exemplos do sistema da biblioteca sempre que possível.
- Não se limite a decorar definições: explique o motivo de cada decisão.
- Quando uma questão solicitar uma proposta de solução, descreva o comportamento esperado antes de pensar no código.

**Objetivo final:** compreender que uma API não deve apenas manipular dados, mas também garantir que as operações respeitem as regras que definem o funcionamento correto do sistema.