from celery import shared_task

@shared_task
def minha_tarefa():
    print("Executando tarefa a cada 5 segundos")
