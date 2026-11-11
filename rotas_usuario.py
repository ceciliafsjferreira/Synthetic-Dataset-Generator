import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random
import requests

fake = Faker('pt_BR')
Faker.seed(42)

hoje = datetime.now()
dados_usuarios = []

for _ in range(3):
    id_usuario = random.randint(1000000, 9999999)
    dias_sem_acesso = random.randint(0, 20)
    estado_perfil = 'Inativo' if dias_sem_acesso > 8 else 'Ativo'
    
    dados_usuarios.append({
        'id_usuario': id_usuario,
        'nome_usuario': fake.name(),
        'nr_cpf': fake.cpf(),
        'email': fake.ascii_free_email(),
        'estado_perfil': estado_perfil,
        'data_cadastro': (hoje - timedelta(days=random.randint(10, 365))).strftime('%Y-%m-%d')
    })

df_usuarios = pd.DataFrame(dados_usuarios)
print("--- Usuários Gerados ---")
print(df_usuarios[['id_usuario', 'nome_usuario']], "\n")


id_1, id_2, id_3 = df_usuarios['id_usuario'].tolist()
nome_1, nome_2, nome_3 = df_usuarios['nome_usuario'].tolist()


rota_1 = {'numero': '8000-10', 'nome': 'Term. Lapa - Pça. Ramos', 'cl': 1234}
rota_2 = {'numero': '8700-10', 'nome': 'Term. Campo Limpo - Pça. Ramos', 'cl': 5678}
rota_3 = {'numero': '2100-10', 'nome': 'Term. Vl. Prudente - Pça. da Sé', 'cl': 9101}

usuarios_favoritos = {
    id_1: {'nome': nome_1, 'rotas': [rota_1, rota_2]},
    id_2: {'nome': nome_2, 'rotas': [rota_3]},
    id_3: {'nome': nome_3, 'rotas': [rota_1, rota_3]}
}


TOKEN_SPTRANS = 'SEU_TOKEN_AQUI'  
URL_BASE = 'http://api.olhovivo.sptrans.com.br/v2.1'

session = requests.Session()

auth_url = f"{URL_BASE}/Login/Autenticar?token={TOKEN_SPTRANS}"
resposta_auth = session.post(auth_url)

if resposta_auth.text == 'true':
    for id_usuario, info in usuarios_favoritos.items():
        print(f"--- Buscando favoritos de {info['nome']} (ID: {id_usuario}) ---")
        
        for rota in info['rotas']:
            posicao_url = f"{URL_BASE}/Posicao?codigoLinha={rota['cl']}"
            resposta = session.get(posicao_url)
            
            if resposta.status_code == 200:
                veiculos = resposta.json().get('vs', [])
                print(f"Linha {rota['numero']}: {len(veiculos)} ônibus operando no momento.")
        print("\n")
else:
    print("Falha na autenticação com o token da SPTrans.")