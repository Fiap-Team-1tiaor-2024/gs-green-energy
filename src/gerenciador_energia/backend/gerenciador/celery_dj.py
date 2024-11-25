from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import schedule

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerenciador.settings')

app = Celery('gerenciador')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'executar-minha-tarefa-cada-5-segundos': {
        'task': 'core.tasks.minha_tarefa',
        'schedule': 5.0,  # Intervalo em segundos
    },
}
