import os
from dotenv import load_dotenv
import pandas as pd
from functions import extrair_dados_previsao, carregar_dados

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
if not BASE_URL:
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
9
LISTA_CIDADES = [
    'Luis Eduardo Magalhaes,BR', 
    'Barreiras,BR',              
    'Balsas,BR',                 
    'Gurupi,BR',
                       
]

if __name__ == "__main__":

    dados_tratados = []

    for cidade in LISTA_CIDADES:
        print(f"Buscando dados para: {cidade}")
        
        dados_brutos = extrair_dados_previsao(cidade, API_KEY, BASE_URL)
        
        if dados_brutos is None:
            print(f"Falha na extração para {cidade}. Pulando...")
            continue
  
    for item in dados_brutos['list']:
        registro = {
            'cidade': dados_brutos['city']['name'],
            'data_previsao': item['dt_txt'],
            'temperatura': item['main']['temp'],
            'umidade': item['main']['humidity'],
            'proba_chuva': round(item.get('pop', 0) * 100, 2),
            'latitude': dados_brutos['city']['coord']['lat'],
            'longitude': dados_brutos['city']['coord']['lon']
        }
        dados_tratados.append(registro)

    clima_df = pd.DataFrame(dados_tratados) 
    

    dados_csv = "dados_climaticos.csv"
    
    cabecalho = not os.path.isfile(dados_csv)
    
    carregar_dados(dados_csv, cabecalho, clima_df)
