from django.db import models

class FonteEnergia(models.Model):
    nome = models.CharField(max_length=100)
    sustentavel = models.BooleanField(default=False)
    url_api = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.nome

class TarifaEnergia(models.Model):
    fonte = models.ForeignKey(FonteEnergia, on_delete=models.CASCADE)
    valor_tarifa = models.DecimalField(max_digits=5, decimal_places=2)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fonte.nome} - R$ {self.valor_tarifa}"

class Habitat(models.Model):
    nome = models.CharField(max_length=100)
    data_hora = models.DateTimeField(auto_now_add=True)
    fonte = models.ForeignKey(FonteEnergia, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.nome}"

class Consumo(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    consumo_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE, null=True)
    tarifa = models.ForeignKey(TarifaEnergia, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.habitat} {self.data_hora} - {self.consumo_kwh} kWh"

def selecionar_melhor_fonte():
    tarifas_atualizadas = TarifaEnergia.objects.filter(data_hora__date=timezone.now().date())
    melhor_tarifa = tarifas_atualizadas.order_by('valor_tarifa').first()
    return melhor_tarifa.fonte if melhor_tarifa else None
