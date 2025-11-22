import requests

def extrair_dados_previsao(cidade, api_key, base_url):
    parametros = {
        "q": cidade,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=parametros)

    if response.status_code == 200:
        print("Conexão bem-sucedida! Dados brutos bem recebidos.")
        return response.json()

    else:
        print(f"Erro na conexão! Status Code: {response.status_code}")
        return None
    
