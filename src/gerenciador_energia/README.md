# Projeto Django, ReactJS, Celery e Redis com Docker Compose

Este projeto é uma aplicação web completa que integra Django (backend), ReactJS (frontend), Celery (tarefas assíncronas) e Redis (broker de mensagens), orquestrados utilizando Docker Compose. O objetivo é fornecer um ambiente de desenvolvimento e testes pronto para uso, facilitando a execução e compreensão da arquitetura e dos componentes envolvidos.


## Arquitetura do Sistema

A arquitetura do sistema é composta por:

    - Frontend: Aplicação ReactJS que fornece a interface do usuário.

    - Backend: Aplicação Django que expõe uma API RESTful e um painel de 
    administração.

    - Tarefas Assíncronas: Celery, integrado com o Django, executa  tarefas em segundo plano.
    Broker de Mensagens: Redis atua como intermediário para as filas de tarefas do Celery.

    - Orquestração: Docker Compose gerencia todos os serviços em contêineres separados.


## Componentes Principais

### Django (Backend)

    Função: Servir a API RESTful e gerenciar a lógica de negócio.
    Porta: 8000
    URL de acesso: http://localhost:8000/admin

### ReactJS (Frontend)

    Função: Interface de usuário para interação com o sistema.
    Porta: 3000
    URL de acesso: http://localhost:3000

### Celery

    Função: Executar tarefas assíncronas em segundo plano.
    Componentes:
        Celery Worker: Executa as tarefas enfileiradas.
        Celery Beat: Agendador de tarefas periódicas.

### Redis

    Função: Broker de mensagens e backend de resultados para o Celery.
    Porta: 6379

## Construir e Iniciar os Contêineres

Execute o seguinte comando para construir as imagens e iniciar os contêineres:

```docker-compose up --build```

Este comando iniciará os seguintes serviços:

    redis
    django
    celery-worker
    celery-beat
    react

## Aplicar Migrações e Criar Superusuário

Em um novo terminal, aplique as migrações do Django e crie o superusuário:

### Aplicar migrações
```docker-compose exec django python manage.py migrate```

### Criar superusuário
```docker-compose exec django python manage.py createsuperuser```

Siga as instruções para definir o usuário e senha. Para este projeto, use:

    Usuário: fiap
    Senha: password

## Acessando a Aplicação

### Frontend (ReactJS)

Acesse o frontend no navegador:

    URL: http://localhost:3000

### Backend (Django Admin)

Acesse o painel administrativo do Django:

    URL: http://localhost:8000/admin
    Usuário: fiap
    Senha: password

## Detalhes dos Componentes

### Django

    Descrição: Framework web em Python que fornece uma plataforma robusta para desenvolvimento rápido.
    Funcionalidades:
        API RESTful para comunicação com o frontend.
        Painel administrativo para gerenciamento dos dados.
        Integração com o Celery para tarefas assíncronas.

### ReactJS

    Descrição: Biblioteca JavaScript para construção de interfaces de usuário.
    Funcionalidades:
        Interface responsiva e dinâmica.
        Consumo da API do backend para exibir e manipular dados.
        Componentes reutilizáveis para melhor manutenção.

### Celery e Celery Beat

    Celery:
        Descrição: Sistema de fila de tarefas distribuídas para processamento assíncrono.
        Funcionalidade: Executa tarefas em segundo plano, como processamento de dados e envio de emails.
    Celery Beat:
        Descrição: Agendador de tarefas periódico para o Celery.
        Funcionalidade: Agenda e despacha tarefas em intervalos definidos.

### Redis

    Descrição: Armazenamento em memória usado como broker e backend de resultados para o Celery.
    Funcionalidade: Intermedia a comunicação entre o Django e o Celery, armazenando tarefas e seus resultados.

Estrutura de Diretórios

```
projeto/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── manage.py
│   ├── gerenciador/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── celery_app.py
│   │   ├── tasks.py
│   │   └── ...
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── src/
│   │   └── index.js
│   └── ...
└── docker-compose.yml

```
    - backend/: Contém a aplicação Django.
    - Dockerfile: Define a imagem Docker para o backend.   
    - requirements.txt: Lista de dependências Python.
    - gerenciador/: Configurações e módulos do Django.
    - celery_app.py: Configuração do Celery.
    - frontend/: Contém a aplicação ReactJS.
    - Dockerfile: Define a imagem Docker para o frontend.
    - package.json: Dependências do Node.js.
    - docker-compose.yml: Orquestra os contêineres Docker.

## Comandos Úteis

###    Iniciar os contêineres em modo desanexado:

```docker-compose up -d```

### Parar os contêineres:

```docker-compose down```

### Ver os logs dos contêineres:

``` docker-compose logs -f ```

### Executar um comando em um contêiner em execução:

``` docker-compose exec nome_do_servico comando```

Exemplo:

```    docker-compose exec django python manage.py makemigrations```

