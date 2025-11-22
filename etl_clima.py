#coletar latitude e longitude
import pandas as pd
from src.functions import extrair_dados_previsao
from config.settings import API_KEY, BASE_URL

LISTA_CIDADES = [
    'Luis Eduardo Magalhaes,BR', 
    'Barreiras,BR',              
    'Balsas,BR',                 
    'Gurupi,BR'                   
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
    
    print(clima_df.head())
        
   
        

   


