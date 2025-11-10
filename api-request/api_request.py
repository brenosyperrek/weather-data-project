import requests

api_key = "9be2aac0d013bc5acf899f1f664d6bea"
api_url = "https://api.weatherstack.com/current?access_key=9{api_key}&query=Florianopolis"

def fetch_weather_data():
    print("Coletando dados meteorológicos de weatherstack.com")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("Informações coletadas com sucesso de weatherstack.com.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição em weatherstack.com: {e}")
        raise
    
def mock_fetch_data():
    return {"request":{"type":"City","query":"Florianopolis, Brazil","language":"en","unit":"m"},"location":{"name":"Florianopolis","country":"Brazil","region":"Santa Catarina","lat":"-27.583","lon":"-48.567","timezone_id":"America\/Sao_Paulo","localtime":"2025-11-10 14:52","localtime_epoch":1762786320,"utc_offset":"-3.0"},"current":{"observation_time":"05:52 PM","temperature":24,"weather_code":116,"weather_icons":["https:\/\/cdn.worldweatheronline.com\/images\/wsymbols01_png_64\/wsymbol_0002_sunny_intervals.png"],"weather_descriptions":["Partly cloudy"],"astro":{"sunrise":"05:17 AM","sunset":"06:40 PM","moonrise":"No moonrise","moonset":"10:00 AM","moon_phase":"Waning Gibbous","moon_illumination":73},"air_quality":{"co":"182.85","no2":"4.05","o3":"88","so2":"1.55","pm2_5":"6.95","pm10":"9.25","us-epa-index":"1","gb-defra-index":"1"},"wind_speed":11,"wind_degree":84,"wind_dir":"E","pressure":1020,"precip":0,"humidity":50,"cloudcover":50,"feelslike":26,"uv_index":10,"visibility":10,"is_day":"yes"}}