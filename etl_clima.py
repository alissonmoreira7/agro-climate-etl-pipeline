from src.functions import extrair_dados_previsao
from config.settings import CIDADE_TESTE, API_KEY, BASE_URL

if __name__ == "__main__":

    dados_brutos = extrair_dados_previsao(CIDADE_TESTE, API_KEY, BASE_URL)

    if dados_brutos is not None:
        print(f"Chaves do JSON: {dados_brutos.keys()}")
       
    else:
        print("A extração falhou. Verifique as credenciais ou a conexão.")

    dados_tratados = []

    for item in dados_brutos['list']:
        registro = {
            'cidade': dados_brutos['city']['name'],
            'data_previsao': item['dt_txt'],
            'temperatura': item['main']['temp'],
            'umidade': item['main']['humidity'],
            'proba_chuva': round(item.get('pop', 0)*100, 2)
        }

        dados_tratados.append(registro)
        

   


