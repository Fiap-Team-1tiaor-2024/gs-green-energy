# Projeto de Análise de Consumo Energético

## 📄 Descrição do Projeto
Este projeto foi desenvolvido para gerenciar e analisar dados relacionados ao consumo energético nos campus da faculdade UFRN (Universidade Federal do Rio Grande do Norte). A base de dados contém informações detalhadas sobre faturas, medições de energia e características das localidades atendidas. A análise dos dados é feita através de queries SQL, com foco em identificar padrões de consumo, valores médios, tendências anuais e regionais.

---

## 🗃️ Estrutura da Tabela `consumo_energetico_rn`

A tabela `consumo_energetico_rn` foi projetada para armazenar informações de consumo energético e possui os seguintes campos:

| Campo                           | Tipo de Dados       | Descrição                                                                 |
|---------------------------------|---------------------|---------------------------------------------------------------------------|
| `id`                            | `NUMBER(15)`        | Identificador único da fatura (chave primária).                           |
| `numero_fatura`                 | `NUMBER(10)`        | Número da fatura associada ao consumo.                                    |
| `localidade`                    | `VARCHAR2(255)`     | Localidade onde ocorreu o consumo.                                        |
| `ano`                           | `NUMBER(4)`         | Ano de referência da fatura.                                              |
| `mes_referencia_fatura`         | `NUMBER(2)`         | Mês de referência da fatura (1 a 12).                                     |
| `tipo_conceito_faturado`        | `VARCHAR2(255)`     | Descrição do conceito faturado, como tarifas ou impostos.                 |
| `quantidade_conceito_faturado`  | `NUMBER(10,2)`      | Quantidade associada ao conceito faturado.                                |
| `valor_conceito_faturado`       | `NUMBER(10,2)`      | Valor financeiro do conceito faturado.                                    |
| `valor_fatura`                  | `NUMBER(10,2)`      | Valor total da fatura.                                                    |
| `data_leitura_anterior`         | `DATE`              | Data da leitura anterior do medidor.                                      |
| `data_leitura_atual`            | `DATE`              | Data da leitura atual do medidor.                                         |
| `tensao`                        | `VARCHAR2(50)`      | Tipo de tensão utilizada (baixa, média, alta).                            |
| `perda_transformacao`           | `NUMBER(5,2)`       | Perda de energia no processo de transformação.                            |
| `fator_potencia`                | `NUMBER(5,2)`       | Fator de potência do sistema.                                             |
| `valor_demanda_contratada_ponta`| `NUMBER(10,2)`      | Valor da demanda contratada na ponta.                                     |
| `valor_demanda_cont_fora_ponta` | `NUMBER(10,2)`      | Valor da demanda contratada fora da ponta.                                |
| `numero_medidor`                | `VARCHAR2(50)`      | Número do medidor associado ao consumo.                                   |
| `campus`                        | `VARCHAR2(255)`     | Campus onde está localizada a medição.                                    |
| `cidade`                        | `VARCHAR2(255)`     | Cidade onde está localizada a medição.                                    |
| `cep`                           | `VARCHAR2(20)`      | CEP da localização.                                                       |

---

## 🔍 Consultas SQL

### 1. **Consultas Básicas**
Consulta de todos os dados da tabela:

- SELECT * FROM consumo_energetico_rn;

Faturas do mês de referência 8:

- SELECT mes_referencia_fatura, numero_fatura FROM consumo_energetico_rn  WHERE mes_referencia_fatura = 8;

### 2. **Análise de Valores Faturados**

Faturas com valor acima de 100:
- SELECT valor_conceito_faturado FROM consumo_energetico_rn WHERE valor_conceito_faturado >= 100;

Faturas com valor abaixo de 100:
- SELECT valor_conceito_faturado FROM consumo_energetico_rn WHERE valor_conceito_faturado <= 100;

### 3. **Demanda Contratada**

Demanda contratada na ponta menor ou igual a 50:
- SELECT valor_demanda_contratada_ponta, numero_medidor FROM consumo_energetico_rn WHERE valor_demanda_contratada_ponta <= 50;

Demanda contratada fora da ponta maior ou igual a 100:
- SELECT valor_demanda_cont_fora_ponta, valor_demanda_contratada_ponta, numero_medidor FROM consumo_energetico_rn WHERE valor_demanda_cont_fora_ponta >= 100;

### 4. **Filtragem por Localidade**

Faturas do CEP 59300-000:
- SELECT cep, campus, mes_referencia_fatura, tipo_conceito_faturado, quantidade_conceito_faturado, valor_conceito_faturado, valor_fatura, data_leitura_anterior FROM consumo_energetico_rn WHERE cep LIKE '59300%';

### 5. **Análise Estatística**

Consumo médio por ano:
- SELECT ano AS ANO, AVG(valor_conceito_faturado) AS CONSUMO_MEDIO FROM consumo_energetico_rn GROUP BY ano ORDER BY ANO;

Consumo médio por fatura:
- SELECT localidade, SUM(valor_conceito_faturado) / COUNT(numero_fatura) AS CONSUMO_MEDIO_POR_FATURA FROM consumo_energetico_rn GROUP BY localidade;

Consumo total por ano e localidade:
- SELECT ano AS ANO, localidade, SUM(valor_conceito_faturado) AS CONSUMO_TOTAL FROM consumo_energetico_rn GROUP BY ano, localidade ORDER BY ANO, localidade;

## 📊 Objetivo do Projeto
O projeto tem como foco:

Analisar dados energéticos para identificar padrões de consumo em diferentes campus da UFRN.
Prover insights estatísticos sobre o consumo médio, consumo total e demanda contratada.
Filtrar dados regionais para entender o impacto de fatores geográficos no consumo energético.

## 🔗 Link da base de dados
Link da base de dados proporcionada pelo Governo: [Base de dados](https://dados.gov.br/dados/conjuntos-dados/consumo-energetico-por-campus)

## 🚀 Como Usar
Crie a tabela consumo_energetico_rn no Oracle SQL Developer usando o script de criação fornecido.
Insira os dados reais ou fictícios na tabela para realizar testes.
Execute as consultas SQL para obter os insights descritos acima.
