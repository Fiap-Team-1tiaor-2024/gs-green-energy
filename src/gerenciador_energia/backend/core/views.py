import plotly.express as px
from django_pandas.io import read_frame


def dashboard(request):
    return ""
'''
    consumo = Consumo.objects.order_by('-data_hora')[:24]
    tarifas = TarifaEnergia.objects.filter(data_hora__date=timezone.now().date())
    melhor_fonte = TarifaEnergia.objects.filter(data_hora__date=timezone.now().date()).order_by('valor_tarifa').first()

    # Gerar gráfico de consumo
    df_consumo = read_frame(consumo)
    fig = px.line(df_consumo, x='data_hora', y='consumo_kwh', title='Consumo nas Últimas 24 Horas')
    grafico_consumo = fig.to_html(full_html=False)

    contexto = {
        'consumo': consumo,
        'tarifas': tarifas,
        'melhor_fonte': melhor_fonte,
        'grafico_consumo': grafico_consumo,
    }
    return render(request, 'core/dashboard.html', contexto)
'''
