from src.functions import extrair_dados_previsao
from config.settings import CIDADE_TESTE, API_KEY, BASE_URL

if __name__ == "__main__":

    dados_brutos = extrair_dados_previsao(CIDADE_TESTE, API_KEY, BASE_URL)

    if dados_brutos is not None:
        print("\n✅ Extração bem-sucedida! Pronto para a Transformação.")
        print(f"Chaves do JSON: {dados_brutos.keys()}")
    else:
        print("❌ A extração falhou. Verifique as credenciais ou a conexão.")

