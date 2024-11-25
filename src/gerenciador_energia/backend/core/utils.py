import requests
from core.models import TarifaEnergia, FonteEnergia, Consumo, Habitat

def atualizar_tarifas():
    # Exemplo de chamada a uma API fictícia
    response = requests.get('https://api.exemplo.com/tarifas')
    dados = response.json()
    for item in dados:
        fonte, _ = FonteEnergia.objects.get_or_create(nome=item['fonte'], sustentavel=item['sustentavel'])
        TarifaEnergia.objects.create(fonte=fonte, valor_tarifa=item['valor'], data_hora=timezone.now())

def atualizar_consumo():
    # Exemplo de leitura de um dispositivo IoT
    response = requests.get('https://api.exemplo.com/consumo')
    dados = response.json()
    Consumo.objects.create(consumo_kwh=dados['consumo'], data_hora=timezone.now())
