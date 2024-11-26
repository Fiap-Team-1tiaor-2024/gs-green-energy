from random import random, uniform
from celery import shared_task
from core.models import Habitat, FonteEnergia, Consumo, TarifaEnergia
from decimal import Decimal

@shared_task
def minha_tarefa():
    print(80*"*")
    for tarifa in TarifaEnergia.objects.all():
        price_variation = uniform(-1,1)
        tarifa.valor_tarifa += Decimal(price_variation)
        if tarifa.valor_tarifa <= 0:
            tarifa.valor_tarifa = 1

        tarifa.save()
        print(f'Nome: {tarifa.fonte.nome} novo preço: { tarifa.valor_tarifa }')
    
    menor_tarifa = TarifaEnergia.objects.order_by('valor_tarifa').first()

    print(80*"*")

    for habitat in Habitat.objects.all():
        consumo = uniform(0,8)
        print(f"novo consumo de: {habitat.nome} : {consumo}")
        print(menor_tarifa.fonte)

        habitat.fonte = menor_tarifa.fonte
        print(habitat.nome, habitat.fonte)
        habitat.save()
        c = Consumo.objects.create(consumo_kwh=consumo, habitat=habitat, tarifa=habitat.fonte.tarifaenergia_set.get())
        c = Consumo.objects.create(consumo_kwh=consumo, habitat=habitat, tarifa=menor_tarifa)
        c.save()


