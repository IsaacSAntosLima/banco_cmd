# Atividade — Regras de Negócio no Backend

**Tema:** Regras de negócio, responsabilidades do backend e integridade do banco de dados.

**Contexto:** Durante o desenvolvimento da API da biblioteca, foram implementadas funcionalidades para cadastrar alunos, livros e empréstimos. Diferentemente de um CRUD simples, o módulo de empréstimos precisa respeitar condições específicas, como verificar se o aluno existe, se o livro está disponível e se ele já foi devolvido.

O objetivo desta atividade é compreender o que são regras de negócio, por que são importantes e como se relacionam com o frontend e o banco de dados.

## Parte 1 — Compreendendo os conceitos

**1. O que são regras de negócio?**
    
```
Regras de negocio são especificações sobre oque é ou não permeitido num negócio. Elas servem para restringir informações ou ate mesmo a utilização de dados e funcionalidades do sistema.
```

Explique, com suas próprias palavras, o que são regras de negócio e apresente dois exemplos relacionados ao sistema da biblioteca.

**2. Qual é a importância das regras de negócio?**

Imagine um sistema que permite cadastrar empréstimos sem verificar se o livro já está emprestado. Quais problemas poderiam acontecer? Explique como as regras de negócio ajudam a evitar essas situações.  
```
No exemplo poderia acontecer de alguem solicitar o emprestimo, o registrando sem ter o livro disponivel. As regras de negocio atuam exatamente neste ponto onde ela define que um emprestimo não pode ser realizado enquanto o livro ja esta em emprestimo.
```
**3. Por que não deixar as regras de negócio somente no frontend?**

Imagine que o frontend bloqueia o botão de empréstimo quando um livro está indisponível.

- Por que essa validação, sozinha, não é suficiente?
- O que aconteceria se alguém fizesse uma requisição diretamente pelo Postman?
- Qual deve ser a responsabilidade do backend nessa situação?
```
Deixar apenas o frontend não é o suficiente ja que ao impor as regras no backend a uma segurança maior de os dados não serem consultados de maneira errada, alem de evitar que a requisiçao feita pelo postman escapasse das regras de negócio. A responsabilidade do backend é de restringir certos acessos ou consulta em sua raiz evitando falhas de acesso no sistema.
```

**4. Qual é a responsabilidade do backend?**

Explique por que o backend precisa validar os dados recebidos e verificar as condições necessárias antes de executar uma operação no banco de dados.
```
O backend precisa validar as informações de forma antecipada para evitar consulsultas de desnessesarias alem de servir como uma segurança contra o acesso de dados no sistema.
```

**5. O que acontece quando uma regra de negócio é violada?**

Quando um aluno tenta emprestar um livro que já está emprestado, o sistema deve simplesmente executar a operação e registrar o problema depois? Justifique sua resposta e explique como a API deve comunicar a situação ao cliente.
```
O correto seria que o sistema não permitisse essa violanção de nenhuma maneira, ja que quebra  a regra de negócio. Em vez de permiter o acesso a API deve apenas responder o usuario que o livro solicitado ja esta em situação de emprestimo.
```

## Parte 2 — Backend versus banco de dados

**6. Qual é a diferença entre regras de negócio e restrições do banco de dados?**

Explique a diferença entre as responsabilidades do backend e as do banco de dados. Considere que ambos podem contribuir para impedir operações inválidas.

```
As reponsabilidades do banco de dados estão relacionadas as consultas dos dados e ao armazenamento dos proprios. Ele possui configurações que restringem certos tipos de consultas em sua configuração oque ja contribui para a consulta de dados invalidos. Ja o backend é a parte de processamento das solicitações do usuario, ele pode validar as operações antes de precisar consultar no banco de dados.
```

**7. Analise os exemplos a seguir e identifique a principal responsabilidade de cada um:**

a) O backend verifica se um aluno está cadastrado antes de realizar um empréstimo.
```
 consultar se o aluno ja é cadastrado
```

b) O banco de dados impede que duas linhas possuam o mesmo valor de chave primária.
```
evitar a redundancia entre as chaves primarias
```

c) O backend verifica se um livro já possui um empréstimo em aberto.
```
 verificar os livros que estão em aberto
```

d) O banco de dados impede que um empréstimo referencie um aluno que não existe, por meio de uma chave estrangeira.
```
evitar que um emprestimo estaja atribuido a um aluno inexistente
```
e) O backend verifica se o empréstimo já foi devolvido antes de aceitar uma nova solicitação de devolução.
```
analisar se o livro ja foi devolvido antes de o emprestar
```
Para cada item, explique sua escolha.

**8. Por que não devemos depender exclusivamente do backend ou exclusivamente do banco de dados para garantir a validade das operações?**

Explique como a aplicação das validações no backend e das restrições adequadas no banco de dados pode contribuir para um sistema mais confiável.
```
Quanto mais forma de validar as informações um sistema possuir mais seguro ele fica. Como por exemplo ter camadas de verificações das consultas bem estruturadas tanto no backend como no banco de dados.
```

## Parte 3 — Aplicando os conceitos à biblioteca

**9. Analise a seguinte situação:**

Dois usuários tentam emprestar o mesmo livro quase simultaneamente. Os dois pedidos verificam que o livro está disponível antes que qualquer um deles registre o empréstimo.

- Qual problema pode acontecer?
- Por que uma simples verificação no backend pode não ser suficiente?
- Que medidas poderiam ajudar a impedir que o livro fosse emprestado duas vezes?
```
Poderia acontecer doos dois usuários passarem pela verificação da dispopnibilidade do livro. a verificação no backend pode não ser suficiente porque os dois pedidos podem fazer a verificação quase ao mesmo tempo e receber a informação de que o livro está disponível. Assim, ambos podem tentar registrar o empréstimo antes que o outro seja concluído.

```

**10. Imagine que a biblioteca decida implementar uma nova regra: cada aluno pode ter, no máximo, três empréstimos em aberto.**

Responda:

a) Qual seria a regra de negócio?
```
Que uma aluno nao pode realizar um emprestimo enquanto ja possuir 3 em aberto
```
b) Em qual camada essa regra deveria ser implementada e por quê?
```
no backend ja que ele seria reponsavel por verificar a quantidade de emprestimos realizado pelo aluno
```

c) Que consulta ao banco de dados poderia ajudar a verificar quantos empréstimos em aberto o aluno possui?
```
SELECT * from emprestimo WHERE id_aluno = (id do aluno)
```

d) O que a API deveria fazer quando o aluno já tivesse atingido o limite?
```
responder que o aluno atingiu o limite de emprestimos simuntaneos
```
**11. Um desenvolvedor implementou a seguinte lógica:**

- O frontend verifica se o livro está disponível.
- O backend recebe a requisição e cadastra o empréstimo sem realizar nenhuma validação.
- O banco de dados possui chaves estrangeiras, mas não verifica se o livro já está emprestado.

Quais são os problemas dessa implementação? Proponha melhorias, indicando a responsabilidade de cada camada.
```
O problema dessa implementação é que o frontend é a única camada que verifica a disponibilidade do livro, enquanto o backend cadastra o empréstimo sem validação, permitindo empréstimos duplicados. O frontend deve informar a disponibilidade e apresentar mensagens de erro; o backend deve validar as requisições e verificar se o livro está disponível; e o banco de dados deve utilizar restrições adequadas para impedir empréstimos duplicados e garantir a segurança dos dados.
```

**12. Diferencie validação de dados e regra de negócio, utilizando exemplos da API da biblioteca.**

Considere situações como receber um identificador inválido, não informar um campo obrigatório ou tentar emprestar um livro que já está emprestado.
```
A validação de dados verifica se as informações recebidas pela API estão corretas e no formato esperado, como impedir o envio de um identificador inválido ou exigir o preenchimento de um campo obrigatório. Já a regra de negócio define as condições de funcionamento do sistema, como impedir que um usuário empreste um livro que já está emprestado. Assim, a validação verifica os dados enviados, enquanto a regra de negócio verifica se a operação solicitada é permitida.
```

## Parte 4 — Reflexão final

**13. Explique o que significa dizer que o backend é responsável por aplicar as regras de negócio da aplicação.**
```
O backend é responsável por aplicar as regras de negócio, ele verifica se as operações solicitadas são permitidas pelo sistema. O frontend apresenta as informações e envia as requisições, o backend valida os dados e aplica as regras, como impedir o empréstimo de um livro já emprestado, e o banco de dados armazena as informações e garante sua segurança por meio de restrições e transações.
```
Sua resposta deve relacionar o frontend, o backend e o banco de dados.

**14. Em sua opinião, qual seria a consequência de implementar uma API que realiza todas as operações de CRUD corretamente, mas não possui regras de negócio?**
```
ela pode permitir operações invalidas, mesmo que o o codigo esteja coerente. Por exemplo, mesmo que todo os codigos estejam corretas ela mainda permitiria que o usuario pudesse fazer varias emprestimos ao mesmo tempo sem limite.
```
Utilize um exemplo concreto para justificar sua resposta.

## Orientações

- Responda com suas próprias palavras.
- Utilize exemplos do sistema da biblioteca sempre que possível.
- Não se limite a decorar definições: explique o motivo de cada decisão.
- Quando uma questão solicitar uma proposta de solução, descreva o comportamento esperado antes de pensar no código.

**Objetivo final:** compreender que uma API não deve apenas manipular dados, mas também garantir que as operações respeitem as regras que definem o funcionamento correto do sistema.