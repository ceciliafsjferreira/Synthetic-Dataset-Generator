import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker('pt_BR')
Faker.seed(42)

num_registros = 10
hoje = datetime.now()
dados_usuarios = []

for _ in range(num_registros):
    id_usuario = random.randint(1000000, 9999999)
    nome_usuario = fake.name()
    nr_cpf = fake.cpf()
    email = fake.ascii_free_email()
    
  
    dias_desde_cadastro = random.randint(10, 365)
    data_cadastro = hoje - timedelta(days=dias_desde_cadastro)
    
    dias_sem_acesso = random.randint(0, 20)
    estado_perfil = 'Inativo' if dias_sem_acesso > 8 else 'Ativo'
    
    dados_usuarios.append({
        'id_usuario': id_usuario,
        'nome_usuario': nome_usuario,
        'nr_cpf': nr_cpf,
        'email': email,
        'estado_perfil': estado_perfil,
        'data_cadastro': data_cadastro.strftime('%Y-%m-%d')
    })

df_usuarios = pd.DataFrame(dados_usuarios)

df_usuarios.to_csv('usuarios_ficticios.csv', index=False, encoding='utf-8')

print(df_usuarios.head())