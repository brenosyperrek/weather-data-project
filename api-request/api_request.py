import requests

api_url = "https://api.weatherstack.com/current?access_key=9be2aac0d013bc5acf899f1f664d6bea&query=Florianopolis"

def fetch_data():
    print("Coletando dados meteorológicos de weatherstack.com")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("Informações coletadas com sucesso de weatherstack.com.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição em weatherstack.com: {e}")
        raise