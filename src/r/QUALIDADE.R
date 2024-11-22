# Instalação de pacotes
install.packages("tidyr")
install.packages("dplyr")
install.packages("gridExtra")

# Importação de bibliotecas
library(tidyr)
library(dplyr)
library(gridExtra)

# Adaptar de acordo com o caminho do arquivo do usuário
setwd("C:/Dev/Projetos/gs-green-energy/src/r/csv")

# Leitura do arquivo
data <- read.csv("sastifacao_consumidor.csv", sep = ";")

# trocar ',' por '.' e converter a coluna para numérica 
data$MdaIndicadorQualidade <- gsub(",", ".", data$MdaIndicadorQualidade)
data$MdaIndicadorQualidade <- as.numeric(data$MdaIndicadorQualidade)

# Calculo da média e Visualização dos dados
media_qualidade <- data %>%  group_by(NumAno) %>% summarize(MEDIA_QUALIDADE = mean(MdaIndicadorQualidade))
print(media_qualidade)

# trocar ',' por '.' e converter a coluna para numérica 
data$MdaIndicadorSatisfacao <- gsub(",", ".", data$MdaIndicadorSatisfacao)
data$MdaIndicadorSatisfacao <- as.numeric(data$MdaIndicadorSatisfacao)

# Calculo da média e Visualização dos dados
media_satisfacao <- data %>%  group_by(NumAno) %>% summarize(MEDIA_SATISFACAO = mean(MdaIndicadorSatisfacao))
print(media_satisfacao)

# trocar ',' por '.' e converter a coluna para numérica 
data$MdaIndicadorFidelidade <- gsub(",", ".", data$MdaIndicadorFidelidade)
data$MdaIndicadorFidelidade <- as.numeric(data$MdaIndicadorFidelidade)

# Substituir valores em branco por 0
data$MdaIndicadorQualidade[data$MdaIndicadorQualidade == ""] <- 0

# Converter a coluna para numérica, se necessário
data$MdaIndicadorQualidade <- as.numeric(data$MdaIndicadorQualidade)

# Verificar a coluna após a substituição
print(data$MdaIndicadorQualidade)

# Calculo da média e Visualização dos dados
media_fidelidade <- data %>%  group_by(NumAno) %>% summarize(MEDIA_FIDELIDADE = mean(MdaIndicadorFidelidade))
print(media_fidelidade)

# trocar ',' por '.' e converter a coluna para numérica 
data$MdaIndicadorValor <- gsub(",", ".", data$MdaIndicadorValor)
data$MdaIndicadorValor <- as.numeric(data$MdaIndicadorValor)

# Calculo da média e Visualização dos dados
media_valor <- data %>%  group_by(NumAno) %>% summarize(MEDIA_VALOR = mean(MdaIndicadorValor))
print(media_valor)

# trocar ',' por '.' e converter a coluna para numérica 
data$MdaIndicadorConfianca <- gsub(",", ".", data$MdaIndicadorConfianca)
data$MdaIndicadorConfianca <- as.numeric(data$MdaIndicadorConfianca)

# Calculo da média e Visualização dos dados
media_confianca <- data %>%  group_by(NumAno) %>% summarize(MEDIA_CONFIANCA = mean(MdaIndicadorConfianca))
print(media_confianca)

# Visualização dos dados e calculo do desvio padrão
desvio_qualidade <- data %>%  group_by(NumAno) %>% summarize(desvio_qualidade = sd(MdaIndicadorQualidade))
desvio_satisfacao <- data %>%  group_by(NumAno) %>% summarize(desvio_satisfacao = sd(MdaIndicadorSatisfacao))
desvio_fidelidade <- data %>%  group_by(NumAno) %>% summarize(desvio_fidelidade = sd(MdaIndicadorFidelidade))
desvio_valor <- data %>%  group_by(NumAno) %>% summarize(desvio_valor = sd(MdaIndicadorValor))
desvio_confianca <- data %>%  group_by(NumAno) %>% summarize(desvio_confianca = sd(MdaIndicadorConfianca))

print(desvio_qualidade)
print(desvio_satisfacao)
print(desvio_fidelidade)
print(desvio_valor)
print(desvio_confianca)