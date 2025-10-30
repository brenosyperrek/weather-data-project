#import requests

#access_key = '9be2aac0d013bc5acf899f1f664d6bea'
#api_url = f'http://api.weatherstack.com/current?access_key={access_key}&query=Florianopolis'

#def fetch_weather_data():
#    print("Iniciando a coleta de dados da API de clima...")
#    try:
#        response = requests.get(api_url)
#        response.raise_for_status()
#        print("Dados coletados com sucesso")
#        return response.json()
#    except requests.exceptions.RequestException as e:
#        print(f"Um erro ocorreu: {e}")
#        raise
    
def mock_fetch_weather_data():
    print("Mock: Iniciando a coleta de dados da API de clima...")
    return {"request":{"type":"City","query":"Florianopolis, Brazil","language":"en","unit":"m"},"location":{"name":"Florianopolis","country":"Brazil","region":"Santa Catarina","lat":"-27.583","lon":"-48.567","timezone_id":"America/Sao_Paulo","localtime":"2025-10-30 10:12","localtime_epoch":1761819120,"utc_offset":"-3.0"},"current":{"observation_time":"01:12 PM","temperature":20,"weather_code":116,"weather_icons":["https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png"],"weather_descriptions":["Partly cloudy"],"astro":{"sunrise":"05:25 AM","sunset":"06:32 PM","moonrise":"12:28 PM","moonset":"01:27 AM","moon_phase":"Waxing Gibbous","moon_illumination":53},"air_quality":{"co":"97.85","no2":"1.65","o3":"80","so2":"1.25","pm2_5":"5.85","pm10":"8.35","us-epa-index":"1","gb-defra-index":"1"},"wind_speed":7,"wind_degree":176,"wind_dir":"S","pressure":1020,"precip":0.2,"humidity":68,"cloudcover":50,"feelslike":20,"uv_index":1,"visibility":10,"is_day":"yes"}}

#mock_fetch_weather_data()