# 1. Imagem Base: Começamos com uma imagem oficial e leve do Python 3.10
FROM python:3.10-slim

# 2. Diretório de Trabalho: Cria uma pasta /app dentro do contêiner para organizar nosso projeto
WORKDIR /app

# 3. Copia e Instala as Dependências: Copia a "lista de compras" e manda o pip instalar tudo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia o Projeto: Copia todos os nossos arquivos (.py, .csv, .pkl) para dentro do contêiner
COPY . .

# 5. Comando de Execução: Define o que acontece quando o contêiner "liga".
# Neste caso, ele vai rodar a simulação completa do Red Team vs Blue Team.
CMD ["python", "red_team_agent.py"]