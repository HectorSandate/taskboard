# Usa Python 3.10 como base
FROM python:3.10

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias y dotenv para manejar variables de entorno
RUN pip install --no-cache-dir -r requirements.txt && pip install python-dotenv

# Copiar el código del backend
COPY . /app/

# Exponer puerto 8000 para Django
EXPOSE 8000

# Comando para ejecutar Django con Gunicorn apuntando a la ubicación correcta
CMD ["gunicorn", "taskmanager.wsgi:application", "--bind", "0.0.0.0:8000"]