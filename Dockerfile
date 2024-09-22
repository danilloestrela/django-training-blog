# Dockerfile
# Use uma imagem base do Python
FROM python:3.10-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para instalar as dependências
COPY requirements.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante da aplicação para o contêiner
COPY . /app/

# Exponha a porta 8000 (a porta padrão para o Django)
EXPOSE 8000

# Execute o comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
