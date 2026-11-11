import requests

url = "http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar"
token = "seu_token_aqui"  

sessao = requests.Session()


resposta = sessao.post(
    url,
    params={"token": token}
)

print("Status HTTP:", resposta.status_code)
print("Resposta da API:", resposta.text)

import requests
import pandas as pd
from datetime import datetime


BASE_URL = "https://api.olhovivo.sptrans.com.br/v2.1"

token = input("Digite seu token da SPTrans: ").strip()


sessao = requests.Session()


resposta = sessao.post(
    f"{BASE_URL}/Login/Autenticar",
    params={"token": token},
    timeout=30
)

resposta.raise_for_status()

if resposta.text.strip().lower() != "true":
    raise RuntimeError("Não foi possível autenticar na API.")

print("Autenticação realizada com sucesso!")


resposta = sessao.get(
    f"{BASE_URL}/Posicao",
    timeout=60
)

resposta.raise_for_status()

dados = resposta.json()

print("Consulta realizada com sucesso!")


registros = []

horario_consulta = datetime.now().isoformat(
    timespec="seconds"
)

for linha in dados.get("l", []):

    for veiculo in linha.get("vs", []):

        registros.append({
            "linha": linha.get("c"),
            "codigo_linha": linha.get("cl"),
            "sentido": linha.get("sl"),
            "prefixo_veiculo": veiculo.get("p"),
            "acessivel": veiculo.get("a"),
            "latitude": veiculo.get("py"),
            "longitude": veiculo.get("px"),
            "horario_posicao": veiculo.get("ta"),
            "horario_consulta": horario_consulta
        })


df = pd.DataFrame(registros)


arquivo = "dataset_onibus_sp.csv"

df.to_csv(
    arquivo,
    index=False,
    encoding="utf-8-sig"
)


print(f"\nTotal de veículos encontrados: {len(df)}")
print(f"Dataset salvo em: {arquivo}")

print("\nPrévia dos dados:")
print(df.head())

print("\nDimensões do dataset:")
print(df.shape)