// ----------------- CRIA��O DA TABELA COM BASE NO CSV -----------------
CREATE TABLE consumo_energetico_rn (
    id NUMBER(15) GENERATED BY DEFAULT ON NULL AS IDENTITY,
    numero_fatura NUMBER(10),
    localidade VARCHAR2(255),
    ano NUMBER(4),
    mes_referencia_fatura NUMBER(2),
    tipo_conceito_faturado VARCHAR2(255),
    quantidade_conceito_faturado NUMBER(10, 2),
    valor_conceito_faturado NUMBER(10, 2),
    valor_fatura NUMBER(10, 2),
    data_leitura_anterior DATE,
    data_leitura_atual DATE,
    tensao VARCHAR2(50),
    perda_transformacao NUMBER(5, 2),
    fator_potencia NUMBER(5, 2),
    valor_demanda_contratada_ponta NUMBER(10, 2),
    valor_demanda_cont_fora_ponta NUMBER(10, 2),
    numero_medidor VARCHAR2(50),
    campus VARCHAR2(255),
    cidade VARCHAR2(255),
    cep VARCHAR2(20),
    PRIMARY KEY (id)
);

// ----------------- DROP TABLE -----------------
DROP TABLE consumo_energetico_rn;

// ----------------- INSERT (EXEMPLO DA BASE DE DADOS CSV) -----------------
INSERT INTO consumo_energetico_rn (
    numero_fatura, localidade, ano, mes_referencia_fatura, tipo_conceito_faturado,
    quantidade_conceito_faturado, valor_conceito_faturado, valor_fatura, 
    data_leitura_anterior, data_leitura_atual, tensao, perda_transformacao, fator_potencia, 
    valor_demanda_contratada_ponta, valor_demanda_cont_fora_ponta, numero_medidor, campus, cidade, cep
) VALUES
(1025332, 'CERES - CAIC�', 2009, 8, 'CONSUMO ATIVO FORA PONTA', 180.00, 1150.25, 15048.21, TO_DATE('2009-07-16', 'YYYY-MM-DD'), TO_DATE('2009-08-14', 'YYYY-MM-DD'), '13800 V', 0.00, 0.00, 50.00, 90.00, '000000000060698864', 'CAMPUS CAIC�', NULL, '59300 000');

// ----------------- SELECT'S  -----------------
SELECT * FROM consumo_energetico_rn;

SELECT mes_referencia_fatura, numero_fatura FROM consumo_energetico_rn WHERE mes_referencia_fatura = 8;

SELECT valor_conceito_faturado FROM consumo_energetico_rn WHERE valor_conceito_faturado >= 100;

SELECT valor_conceito_faturado FROM consumo_energetico_rn WHERE valor_conceito_faturado <= 100;

SELECT valor_demanda_contratada_ponta, numero_medidor FROM consumo_energetico_rn WHERE valor_demanda_contratada_ponta <= 50;

SELECT valor_demanda_cont_fora_ponta, valor_demanda_contratada_ponta, numero_medidor FROM consumo_energetico_rn WHERE valor_demanda_cont_fora_ponta >= 100;

SELECT cep, campus, mes_referencia_fatura, tipo_conceito_faturado, quantidade_conceito_faturado, valor_conceito_faturado, valor_fatura, data_leitura_anterior FROM consumo_energetico_rn WHERE cep LIKE '59300 000%';

SELECT tipo_conceito_faturado, quantidade_conceito_faturado, localidade, valor_fatura FROM consumo_energetico_rn WHERE tipo_conceito_faturado LIKE 'PIS/PASEP%';

SELECT numero_fatura, localidade, mes_referencia_fatura, valor_conceito_faturado, valor_fatura, data_leitura_anterior, data_leitura_atual FROM consumo_energetico_rn;

SELECT numero_fatura, localidade, mes_referencia_fatura, valor_conceito_faturado, valor_fatura, data_leitura_anterior, data_leitura_atual FROM consumo_energetico_rn WHERE localidade LIKE 'CERES - CURRAIS NOVOS%';

SELECT numero_fatura, localidade, mes_referencia_fatura, valor_conceito_faturado, valor_fatura, data_leitura_anterior, data_leitura_atual FROM consumo_energetico_rn WHERE localidade LIKE 'CERES - CAIC�%';

// ----------------- SELECT ANALISANDO O CONUMO MEDIO DO VALOR CONCEITO FATURADO  -----------------
SELECT 
    ano AS ANO, 
    AVG(valor_conceito_faturado) AS CONSUMO_MEDIO
FROM 
    consumo_energetico_rn
GROUP BY 
    ano
ORDER BY 
    ANO;

// ----------------- SELECT ANALISANDO O CONUMO MEDIO POR FATURA  -----------------
SELECT 
    localidade, 
    SUM(valor_conceito_faturado) / COUNT(numero_fatura) AS CONSUMO_MEDIO_POR_FATURA
FROM 
    consumo_energetico_rn
GROUP BY 
    localidade;

// ----------------- SELECT ANALISANDO O CONUMO TOTAL FATURADO -----------------
SELECT 
    ano AS ANO, 
    localidade,
    SUM(valor_conceito_faturado) AS CONSUMO_TOTAL
FROM 
    consumo_energetico_rn
GROUP BY 
    ano, localidade
ORDER BY 
    ANO, localidade;
    



