# S203
Repositório referente a matéria de Arquitetura de Software e desenvolvimento da aplicação "Neide's"


## Instalação

### Pré-requisitos

- Python 3.8+
- Django 3.2+
- Pillow (para manipulação de imagens)

### Passos para Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/projeto-neides.git
    cd projeto-neides
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Crie um superusuário:
    ```sh
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

7. Acesse a aplicação em `http://127.0.0.1:8000`.
