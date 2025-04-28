# Nome do ambiente virtual
VENV_NAME=venv

# Cria o ambiente virtual
create_venv:
	python3 -m venv $(VENV_NAME)

# Ativa o venv e instala dependências
install:
	$(VENV_NAME)/bin/pip install --upgrade pip
	$(VENV_NAME)/bin/pip install -r requirements.txt

# Ativa ambiente e roda o projeto
start:
	$(VENV_NAME)/bin/python main.py

# Remove o ambiente virtual
clean:
	rm -rf $(VENV_NAME)

# Cria venv + instala + roda (tudo de uma vez)
setup: create_venv install start
