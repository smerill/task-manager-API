# 📝 Task Manager API

API RESTful de gerenciamento de tarefas, desenvolvida com **FastAPI** e **SQLite**.  
Ideal para praticar conceitos de back-end, arquitetura de APIs, banco de dados relacional e integração com front-ends modernos como React.

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) — Web framework moderno e assíncrono  
- [Uvicorn](https://www.uvicorn.org/) — Servidor ASGI leve e rápido  
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM para banco de dados relacional  
- [Pydantic v2](https://docs.pydantic.dev/latest/) — Validação e serialização de dados  
- SQLite — Banco de dados local simples  
- Python 3.11+

## 🎯 Funcionalidades

✅ Cadastro de tarefas  
✅ Listagem de tarefas  
✅ Atualização de tarefas  
✅ Remoção de tarefas  
✅ Respostas em JSON  
✅ Documentação interativa automática via Swagger (`/docs`)

## 🛠️ Como executar o projeto

1. Clone o repositório:
    git clone https://github.com/smerill/task-manager-api.git
2. Crie e ative um ambiente virutal:
    python -m venv .venv
    .venv\Scripts\activate # windows
    .venv/bin/activate # linux/macOS
3. Instale as dependências:
    pip install -r requirements.txt
4. Execute a aplicação:
    uvicorn app.main:app --reload
5. Acesse a API no navegador:
    http://127.0.0.1:8000
    http://127.0.0.1:8000/docs → interface Swagger (interativa)
    http://127.0.0.1:8000/redoc → documentação Redoc

## ✨ Futuras melhorias

- Autenticação com JWT
- Integração com PostgreSQL
- Deploy na nuvem
- Integração com front-end em React + Tailwind
- Filtro de tarefas por status (concluída / pendente)
