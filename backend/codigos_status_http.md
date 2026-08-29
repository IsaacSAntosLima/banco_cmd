## **1xx**
```
O servidor faz um aviso sobre o inicio ou o recebimento dos dados.Um exemplo é o código 100 Continue, que informa ao cliente que ele pode continuar enviando a requisição.
```
## **2xx**
```
O servidor faz um aviso sobre a conclusão da requisição realizada. Um exemplo é o 200 OK, que indica que a requisição foi processada com sucesso.
```
## **3xx**
```
O servidor informa que algo esta pendente e tem que ser alterado antes da ação ser realizada. Um exemplo é o 301 Moved Permanently, que indica que um recurso foi movido permanentemente para outra URL.
```
## **4xx**
```
O servidor faz um aviso sobre um possivel erro na requisição. Um exemplo é o 404 Not Found, utilizado quando o recurso solicitado não foi encontrado.
```
## **5xx**
```
O servidor falhou no processamento. Um exemplo é o 500 Internal Server Error, que indica um erro interno inesperado no servidor.
```
## Principais códigos

## **200 ok**
```
Significa que a requisição foi realizada com sucesso. Ele deve ser utilizado quando uma operação foi concluída corretamente e uma resposta é retornada ao cliente. Por exemplo, quando o usuário consulta um livro, a API pode encontrar o livro e retornar seus dados utilizando o código 200 OK.
```
## **201**
```
Significa que algo foi criado. Ele deve ser utilizado principalmente depois de uma requisição responsável pela criação de um recurso. Por exemplo, quando o usuário envia os dados de um livro para a API cadastra esse livro corretamente, ela pode retornar 201 Created, informando que o novo livro foi criado.
```
## **204**
```
O código 204 No Content significa que a requisição foi realizada com sucesso, mas o servidor não possui conteúdo para retornar no corpo da resposta. Ele pode ser utilizado, por exemplo, quando um livro é atualizado ou excluído e a API não precisa enviar informações adicionais ao cliente. Nesse caso, a operação é concluída corretamente, mas nenhuma informação é retornada no corpo da resposta.
```
## **400**
```
O código 400 Bad Request significa que o servidor não conseguiu processar a requisição porque ela possui algum problema. Ele deve ser utilizado quando os dados enviados pelo cliente estão incorretos, incompletos ou malformados. Por exemplo, ao tentar cadastrar um livro, o usuário pode enviar um JSON inválido ou deixar uma estrutura de dados incompleta. Nesse caso, a API pode retornar 400 Bad Request informando que a requisição é inválida.
```
## **401**
```
O código 401 Unauthorized significa que o cliente não está autenticado corretamente. Ele deve ser utilizado quando a API exige autenticação, como um login, mas o usuário não forneceu uma credencial válida. Por exemplo, se somente usuários autenticados podem cadastrar livros e uma pessoa tenta utilizar sem fornecer a informação necessária, a API pode retornar 401 Unauthorized.
```
## **403**
```
O código 403 Forbidden significa que o cliente está autenticado, mas não possui permissão para realizar determinada ação. Ele deve ser utilizado quando o usuário possui uma conta válida, porém não tem autorização suficiente. Por exemplo, se somente bibliotecários podem cadastrar livros e um usuário comum tentar cadastrar um livro, a API pode retornar 403 Forbidden, indicando que ele não possui permissão para realizar o cadastro.
```
## **404**
```
O código 404 Not Found significa que o recurso solicitado não foi encontrado. Ele deve ser utilizado quando o cliente tenta acessar um recurso que não existe. Por exemplo, se o usuário tentar alterar um livro com o id 9999, mas não existir nenhum livro com o ID 9999, a API pode retornar 404 Not Found.
```
## **409**
```
O código 409 Conflict significa que existe um conflito entre a requisição e o estado atual dos dados no servidor. Ele deve ser utilizado quando a operação não pode ser realizada porque existe alguma informação conflitante. Por exemplo, se a API não permitir que dois livros tenham o mesmo id e o usuário tentar cadastrar um livro com um id que já está registrado, a API pode retornar 409 Conflict, informando que aquele ISBN já está cadastrado.
```
## **500**
```
O código 500 Internal Server Error significa que ocorreu um erro inesperado dentro do servidor. Ele deve ser utilizado quando a API encontra uma falha interna que impede o processamento da requisição. Por exemplo, o usuário pode enviar corretamente todos os dados para cadastrar um livro, mas ocorrer uma falha inesperada no sistema ou no banco de dados. Nesse caso, a API pode retornar 500 Internal Server Error.
```
## **503**
```
O código 503 Service Unavailable significa que o servidor está temporariamente indisponível ou não está preparado para processar a requisição naquele momento. Ele deve ser utilizado principalmente durante situações como manutenção, sobrecarga ou indisponibilidade temporária de algum serviço. Por exemplo, se o usuário tentar cadastrar um livro enquanto a API estiver em manutenção, ela pode retornar 503 Service Unavailable, indicando que o serviço está temporariamente indisponível.
```

