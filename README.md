# 🎲 Synthetic Dataset Generator — Criação de Dataset Fictício em Python

> Script em Python desenvolvido para gerar um conjunto de dados sintéticos e estruturados, ideal para testes de pipelines de dados, modelagem preditiva, validação de schemas e análises exploratórias sem expor dados reais ou sensíveis.

---

## 🎯 Objetivo do Projeto

Ao trabalhar com projetos de Data Science e Engenharia de Dados, muitas vezes precisamos de dados estruturados para homologação de ambientes ou treinamento de modelos antes da integração com bases reais. 

Este script automatiza a criação de um dataset fictício com dados populados de forma estocástica e consistente, simulando cenários reais de negócios.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Manipulação de Dados:** Pandas / NumPy
* **Geração de Dados Sintéticos:** Faker *(ou substitua pelas bibliotecas que usou)*
* **Exportação:** CSV / Parquet

---

## 📋 Estrutura do Dataset Gerado

O script gera um arquivo final contendo as seguintes variáveis simuladas:

| Coluna | Tipo de Dado | Descrição | Exemplo |
| :--- | :--- | :--- | :--- |
| `id_cliente` | String / UUID | Identificador único do registro | `CLI-83920` |
| `data_registro` | Datetime | Data e hora da ocorrência | `2024-05-12 14:30:00` |
| `categoria` | Categorização | Categoria simulada | `Eletrônicos` |
| `valor` | Float | Valor numérico gerado | `154.50` |
| `status` | Categorização | Estado da transação/registro | `Concluído` |

---

## 🚀 Como Executar o Script

### Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina.
