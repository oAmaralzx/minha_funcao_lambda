 minha_funcao_lambda
**Função Lambda - Calculadora**

Esta função AWS Lambda realiza operações matemáticas básicas (`soma`, `subtracao`, `multiplicacao`, `divisao`) a partir de um JSON enviado via requisição HTTP POST. Ela está integrada a uma **Lambda Function URL**.


**Requisitos e Dependências**

Esta função foi escrita em Python 3.13 e não depende de bibliotecas externas além da biblioteca padrão do Python.


**Como Testar a Função**

**Enviando a Requisição**

Você pode usar o Postman, Insomnia ou qualquer outro cliente HTTP para enviar um `POST` para a URL da função Lambda:

URL da função Lambda:
https://7xalj6inthpn5wsn3axtrpfva40rqmzy.lambda-url.us-east-2.on.aws/

**Configuração no Postman**

Método: `POST`
  - Headers:
  - `Content-Type`: `application/json`
  - Body:
  - Selecione a opção `raw`
  - Escolha `JSON` no menu suspenso à direita
  - Corpo da requisição:

```json do evento
{
  "operacao": "soma",
  "numero1": 10,
  "numero2": 5
}
