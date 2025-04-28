# How to test

- python3 main.py
- old version - using falskapi: python3 api/api_server.py
- python3 -m uvicorn api.api_server:app --reload

# Makefile

- Criar venv | make create_venv
- Instalar dependências | make install
- Rodar o projeto | make start
- Limpar ambiente virtual | make clean
- Fazer tudo de uma vez (setup completo) | make setup
