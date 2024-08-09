# Dados simulados
cidades = [
    {"id_cidade": 1, "nome": "São Paulo", "estado": "SP"},
    {"id_cidade": 2, "nome": "Rio de Janeiro", "estado": "RJ"}
]

pessoas = [
    {"id_pessoa": 1, "nome": "Ana", "id_cidade": 1},
    {"id_pessoa": 2, "nome": "Carlos", "id_cidade": 2}
]

telefones = [
    {"id_pessoa": 1, "numero": "1234-5678"},
    {"id_pessoa": 2, "numero": "8765-4321"}
]

emails = [
    {"id_pessoa": 1, "email": "ana@email.com"},
    {"id_pessoa": 2, "email": "carlos@email.com"}
]

def obter_dados_pessoa(id_pessoa:int) -> dict:
    pessoa_dados = None
    cidade_dados = None
    telefone_dados = None
    email_dados = None
    
    for pessoa in pessoas:
        if pessoa["id_pessoa"] == id_pessoa:
            pessoa_dados = pessoa
            break
    
    if pessoa_dados:
        for cidade in cidades:
            if cidade["id_cidade"] == pessoa_dados["id_cidade"]:
                cidade_dados = cidade
                break
        
        telefone_dados = [telefone["numero"] for telefone in telefones if telefone["id_pessoa"] == id_pessoa]

        email_dados = [email["email"] for email in emails if email["id_pessoa"] == id_pessoa]

    return {
        "Pessoa": pessoa_dados,
        "Cidade": cidade_dados,
        "Telefones": telefone_dados,
        "Emails": email_dados
    }

# Exemplo de uso
id_pessoa = 2
dados = obter_dados_pessoa(id_pessoa)
for key, value in dados.items():
    print(f"{key}: {value}")
