import requests
import json

api_key ="sua_chave_aqui"  
lat = "-23.5505" 
lon = "-46.6333" 

url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    nome_cidade = dados['city']['name']
    
    print(f"--- Previsão para {nome_cidade} ---")
    
   
    for previsao in dados['list']:
     
        data_hora = previsao['dt_txt'] 
        
       
        temperatura = previsao['main']['temp']
        descricao = previsao['weather'][0]['description']
        chuva_1h = dados.get('rain', {}).get('1h', 0)
        vento_ms = dados.get('wind', {}).get('speed', 0)
        
        print(f"{data_hora} | {temperatura}°C | {descricao.capitalize()}")

    else:
        print(f"Erro: {response.status_code}")
        print(response.text)


dados = response.json()

with open("previsao_tempo.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print("Arquivo JSON gerado com sucesso!")