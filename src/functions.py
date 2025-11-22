import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

def extrair_dados_previsao(cidade, api_key, base_url,):
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
    
def carregar_dados(conexao, df):

    engine = create_engine(conexao) 
    
    
    df.to_sql(
        name='previsao_clima', 
        con=engine,
        if_exists='append', 
        index=False,
        chunksize=5000
    )
    print("Carga (L) no MySQL concluída com sucesso!")
        
