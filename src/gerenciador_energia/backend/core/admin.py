from django.contrib import admin
from core.models import FonteEnergia, TarifaEnergia , Habitat, Consumo

@admin.register(FonteEnergia)
class FonteEnergiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sustentavel')  

@admin.register(TarifaEnergia)
class TarifaEnergiaAdmin(admin.ModelAdmin):
    list_display = ('fonte', 'valor_tarifa')  

@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ('nome','fonte')  

@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    list_display = ('data_hora', 'habitat', 'consumo_kwh', 'tarifa')  