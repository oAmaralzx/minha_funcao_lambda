import json

def lambda_handler(event, context):
    try:
        print("Evento recebido:", json.dumps(event))  # DEBUG

        # Garante que estamos extraindo o JSON corretamente
        if "body" in event:
            if isinstance(event["body"], str):
                dados = json.loads(event["body"])
            elif isinstance(event["body"], dict):
                dados = event["body"]
            else:
                return {
                    "statusCode": 400,
                    "body": json.dumps("Corpo inválido")
                }
        else:
            return {
                "statusCode": 400,
                "body": json.dumps("Requisição inválida: corpo ausente")
            }

        operacao = dados.get("operacao")
        num1 = dados.get("numero1")
        num2 = dados.get("numero2")

        if not operacao or num1 is None or num2 is None:
            return {
                "statusCode": 400,
                "body": json.dumps("Parâmetros obrigatórios: operacao, numero1, numero2")
            }

        # Realiza a operação solicitada
        if operacao == "soma":
            resultado = num1 + num2
        elif operacao == "subtracao":
            resultado = num1 - num2
        elif operacao == "multiplicacao":
            resultado = num1 * num2
        elif operacao == "divisao":
            if num2 == 0:
                return {
                    "statusCode": 400,
                    "body": json.dumps("Erro: divisão por zero")
                }
            resultado = num1 / num2
        else:
            return {
                "statusCode": 400,
                "body": json.dumps(f"Operação '{operacao}' não suportada")
            }

        return {
            "statusCode": 200,
            "body": json.dumps({"resultado": resultado})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"Erro interno: {str(e)}")
        }